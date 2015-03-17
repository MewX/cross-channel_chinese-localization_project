#define N_LZSS         4096    /* size of ring buffer */
#define F_LZSS           18    /* upper limit for match_length */
#define THRESHOLD    2  /* encode string into position and length
                           if match_length is greater than this */
#define NIL            N_LZSS    /* index for root of binary search trees */

static unsigned long int
        textsize = 0,    /* text size counter */
        codesize = 0,    /* code size counter */
        printcount = 0;    /* counter for reporting progress every 1K bytes */
static unsigned char
        text_buf[N_LZSS + F_LZSS - 1];    /* ring buffer of size N_LZSS,
            with extra F_LZSS-1 bytes to facilitate string comparison */
static int        match_position, match_length,  /* of longest match.  These are
            set by the InsertNode() procedure. */
        lson[N_LZSS + 1], rson[N_LZSS + 257], dad[N_LZSS + 1];  /* left & right children &
            parents -- These constitute binary search trees. */

static void InitTree(void)  /* initialize trees */
{
    int  i;

    /* For i = 0 to N_LZSS - 1, rson[i] and lson[i] will be the right and
       left children of node i.  These nodes need not be initialized.
       Also, dad[i] is the parent of node i.  These are initialized to
       NIL (= N_LZSS), which stands for 'not used.'
       For i = 0 to 255, rson[N_LZSS + i + 1] is the root of the tree
       for strings that begin with character i.  These are initialized
       to NIL.  Note there are 256 trees. */

    for (i = N_LZSS + 1; i <= N_LZSS + 256; i++) rson[i] = NIL;
    for (i = 0; i < N_LZSS; i++) dad[i] = NIL;
}

static void InsertNode(int r)
    /* Inserts string of length F_LZSS, text_buf[r..r+F_LZSS-1], into one of the
       trees (text_buf[r]'th tree) and returns the longest-match position
       and length via the global variables match_position and match_length.
       If match_length = F_LZSS, then removes the old node in favor of the new
       one, because the old one will be deleted sooner.
       Note r plays double role, as tree node and position in buffer. */
{
    int  i, p, cmp;
    unsigned char  *key;

    cmp = 1;  key = &text_buf[r];  p = N_LZSS + 1 + key[0];
    rson[r] = lson[r] = NIL;  match_length = 0;
    for ( ; ; ) {
        if (cmp >= 0) {
            if (rson[p] != NIL) p = rson[p];
            else {  rson[p] = r;  dad[r] = p;  return;  }
        } else {
            if (lson[p] != NIL) p = lson[p];
            else {  lson[p] = r;  dad[r] = p;  return;  }
        }
        for (i = 1; i < F_LZSS; i++)
            if ((cmp = key[i] - text_buf[p + i]) != 0)  break;
        if (i > match_length) {
            match_position = p;
            if ((match_length = i) >= F_LZSS)  break;
        }
    }
    dad[r] = dad[p];  lson[r] = lson[p];  rson[r] = rson[p];
    dad[lson[p]] = r;  dad[rson[p]] = r;
    if (rson[dad[p]] == p) rson[dad[p]] = r;
    else                  lson[dad[p]] = r;
    dad[p] = NIL;  /* remove p */
}

static void DeleteNode(int p)  /* deletes node p from tree */
{
    int  q;
    
    if (dad[p] == NIL) return;  /* not in tree */
    if (rson[p] == NIL) q = lson[p];
    else if (lson[p] == NIL) q = rson[p];
    else {
        q = lson[p];
        if (rson[q] != NIL) {
            do {  q = rson[q];  } while (rson[q] != NIL);
            rson[dad[q]] = lson[q];  dad[lson[q]] = dad[q];
            lson[q] = lson[p];  dad[lson[p]] = q;
        }
        rson[q] = rson[p];  dad[rson[p]] = q;
    }
    dad[q] = dad[p];
    if (rson[dad[p]] == p) rson[dad[p]] = q;  else lson[dad[p]] = q;
    dad[p] = NIL;
}

static void LZSS_Encode( unsigned char *buff,       // 输入文件正文的array
				  unsigned long  len_main,        // 正文的长度
				  unsigned char **out_buff,  // 输出文件的正文array (指向指针的指针)
				  unsigned long *out_len )   // 输出文件长度
{
	*out_buff = new unsigned char [ len_main / 8 + len_main + 1 ]; // large enough for safe
	*out_len = 0;
	unsigned int index_buff = 0;

    int  i, c, len, r, s, last_match_length, code_buf_ptr;
    unsigned char  code_buf[17], mask;
    
	textsize = 0, codesize = 0, printcount = 0;  

    InitTree();  /* initialize trees */
    code_buf[0] = 0;  /* code_buf[1..16] saves eight units of code, and
        code_buf[0] works as eight flags, "1" representing that the unit
        is an unencoded letter (1 byte), "0" a position-and-length pair
        (2 bytes).  Thus, eight units require at most 16 bytes of code. */
    code_buf_ptr = mask = 1;
    s = 0;  r = N_LZSS - F_LZSS;
    for (i = s; i < r; i++) text_buf[i] = ' ';  /* Clear the buffer with
        any character that will appear often. */
    for (len = 0; len < F_LZSS && index_buff < len_main ; len++) {
		c = buff[ index_buff ++ ];
        text_buf[r + len] = c;  /* Read F_LZSS bytes into the last F_LZSS bytes of the buffer */
	}
    if ((textsize = len) == 0) return;  /* text of size zero */
    for (i = 1; i <= F_LZSS; i++) InsertNode(r - i);  /* Insert the F_LZSS strings,
        each of which begins with one or more 'space' characters.  Note
        the order in which these strings are inserted.  This way,
        degenerate trees will be less likely to occur. */
    InsertNode(r);  /* Finally, insert the whole string just read.  The
        global variables match_length and match_position are set. */
    do {
        if (match_length > len) match_length = len;  /* match_length
            may be spuriously long near the end of text. */
        if (match_length <= THRESHOLD) {
            match_length = 1;  /* Not long enough match.  Send one byte. */
            code_buf[0] |= mask;  /* 'send one byte' flag */
            code_buf[code_buf_ptr++] = text_buf[r];  /* Send uncoded. */
        } else {
            code_buf[code_buf_ptr++] = (unsigned char) match_position;
            code_buf[code_buf_ptr++] = (unsigned char)
                (((match_position >> 4) & 0xf0)
             | (match_length - (THRESHOLD + 1)));  /* Send position and
                    length pair. Note match_length > THRESHOLD. */
        }
        if ((mask <<= 1) == 0) {  /* Shift mask left one bit. */
            for (i = 0; i < code_buf_ptr; i++)  /* Send at most 8 units of */
                (*out_buff)[ ( *out_len ) ++ ] = code_buf[ i ];    /* code together */
            codesize += code_buf_ptr;
            code_buf[0] = 0;  code_buf_ptr = mask = 1;
        }
        last_match_length = match_length;
        for (i = 0; i < last_match_length && index_buff < len_main; i++) {
			c = buff[ index_buff ++ ];
            DeleteNode(s);        /* Delete old strings and */
            text_buf[s] = c;    /* read new bytes */
            if (s < F_LZSS - 1) text_buf[s + N_LZSS] = c;  /* If the position is
                near the end of buffer, extend the buffer to make
                string comparison easier. */
            s = (s + 1) & (N_LZSS - 1);  r = (r + 1) & (N_LZSS - 1);
                /* Since this is a ring buffer, increment the position
                   modulo N_LZSS. */
            InsertNode(r);    /* Register the string in text_buf[r..r+F_LZSS-1] */
        }
        if ((textsize += i) > printcount) {
            printf("%12ld\r", textsize);  printcount += 1024;
                /* Reports progress each time the textsize exceeds
                   multiples of 1024. */
        }
        while (i++ < last_match_length) {    /* After the end of text, */
            DeleteNode(s);                    /* no need to read, but */
            s = (s + 1) & (N_LZSS - 1);  r = (r + 1) & (N_LZSS - 1);
            if (--len) InsertNode(r);        /* buffer may not be empty. */
        }
    } while (len > 0);    /* until length of string to be processed is zero */
    if (code_buf_ptr > 1) {        /* Send remaining code. */
        for (i = 0; i < code_buf_ptr; i++) (*out_buff)[ ( *out_len ) ++ ] = code_buf[ i ];
        codesize += code_buf_ptr;
    }
    printf("In : %ld bytes\n", textsize);    /* Encoding is done. */
    printf("Out: %ld bytes\n", codesize);
    printf("Out/In: %.3f\n", (double)codesize / textsize);
}
