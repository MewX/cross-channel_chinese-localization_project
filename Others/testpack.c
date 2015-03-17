#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

#pragma pack( 1 )

typedef struct {
	unsigned long section_count; // 区段数
} ARCHDR; // 归档头部

typedef struct {
	char          type[ 4 ];   // "PNG", "MOS", "OGG"
	unsigned long entry_count; // 文件数
	unsigned long toc_offset;  // 开始处的偏移地址
} ARCSECTHDR; // 归档区段细节

typedef struct {
	char          filename[ 13 ];
	unsigned long length; // 文件长度
	unsigned long offset; // 文件开始处偏移地址
} ARCENTRY; // 文件细节

int main( )
{

	// Chip_E.arc
	{
		int FileCount = 0, i, SectId, EntryId;
		char *FileDetail;
		FILE *f_arc, *f_chs, *f_in;
		ARCHDR ArcHdr;
		ARCSECTHDR *ArcSectHdr;
		ARCENTRY *ArcEntry;
	fprintf( stderr, "\n>> Chip_E.arc\n" );
		
		f_arc = fopen( "Chip_E.arc", "rb" );
		f_chs = fopen( "Chip_E.chs", "wb" );
		if( f_arc == NULL || f_chs == NULL ) return 0; // ERROR01: fail to open
	fprintf( stderr, "1" );

		// Read all info
		fread( &ArcHdr, sizeof( ARCHDR ), 1, f_arc ); // 1
	fprintf( stderr, "[%d]", ArcHdr.section_count );
		ArcSectHdr = (ARCSECTHDR *)malloc( ArcHdr.section_count * sizeof( ARCSECTHDR ) );
		fread( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_arc ); // 2
		for( i = 0; i < ArcHdr.section_count; i ++ ) FileCount += ArcSectHdr[ i ].entry_count;
		ArcEntry = (ARCENTRY *)malloc( FileCount * sizeof( ARCENTRY ) );
		fread( ArcEntry, sizeof( ARCENTRY ), FileCount, f_arc ); // 3
	fprintf( stderr, "2" );

		// Write all info
		fwrite( &ArcHdr, sizeof( ARCHDR ), 1, f_chs ); // 1
		fwrite( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_chs ); // 2
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs ); // 3, need to change then
	fprintf( stderr, "3" );

		// Calc replacement position
		// EFCCA0030.PNG
		for( SectId = 0; SectId < ArcHdr.section_count; SectId ++ ) if( !strcmp( ArcSectHdr[ SectId ].type, "PNG" ) ) break;
	fprintf( stderr, ".(SectId=%d)", SectId );
		if( SectId == ArcHdr.section_count ) return 0; // ERROR02
		for( i = EntryId = 0; i < SectId; i ++ ) EntryId += ArcSectHdr[ i ].entry_count;
	fprintf( stderr, "(~%d/%d)", EntryId, FileCount );
		for( ; EntryId < FileCount; EntryId ++ ) {
			fprintf( stderr, "\n%d:%s", EntryId, ArcEntry[ EntryId ].filename );
			if( !strcmp( ArcEntry[ EntryId ].filename, "EFCCA0030" ) ) break;
		}
	fprintf( stderr, "(=%d/%d)", EntryId, FileCount );
		if( EntryId == FileCount ) return 0; // ERROR03
	fprintf( stderr, "4" );

		// Write files
		for( i = 0; i < FileCount; i ++ ) {
			int FileSize;
			if( i == EntryId ) { // Need to replace
				f_in = fopen( "Chip_E_arc\\EFCCA0030.PNG", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else {
				FileSize = ArcEntry[ i ].length;
				FileDetail = (char *)malloc( FileSize );
				fseek( f_arc, ArcEntry[ i ].offset, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_arc );
			}
			
			fwrite( FileDetail, 1, FileSize, f_chs );
			
			free( FileDetail );
		}
	fprintf( stderr, "5" );
		// ReCalc header info
		for( i = 1; i < FileCount; i ++ )
			ArcEntry[ i ].offset = ArcEntry[ i - 1 ].offset + ArcEntry[ i - 1 ].length;
		fseek( f_chs, sizeof( ARCHDR ) + ArcHdr.section_count * sizeof( ARCSECTHDR ), SEEK_SET );
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs );
		
		
		free( ArcSectHdr );
		free( ArcEntry );
		
		fclose( f_arc );
		fclose( f_chs );
	}








	// Chip_S.arc
	{
		int FileCount = 0, i, SectId1, EntryId1, SectId2, EntryId2;
		char *FileDetail;
		FILE *f_arc, *f_chs, *f_in;
		ARCHDR ArcHdr;
		ARCSECTHDR *ArcSectHdr;
		ARCENTRY *ArcEntry;
	fprintf( stderr, "\n>> Chip_S.arc\n" );
		
		f_arc = fopen( "Chip_S.arc", "rb" );
		f_chs = fopen( "Chip_S.chs", "wb" );
		if( f_arc == NULL || f_chs == NULL ) return 0; // ERROR01: fail to open
	fprintf( stderr, "1" );

		// Read all info
		fread( &ArcHdr, sizeof( ARCHDR ), 1, f_arc ); // 1
	fprintf( stderr, "[%d]", ArcHdr.section_count );
		ArcSectHdr = (ARCSECTHDR *)malloc( ArcHdr.section_count * sizeof( ARCSECTHDR ) );
		fread( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_arc ); // 2
		for( i = 0; i < ArcHdr.section_count; i ++ ) FileCount += ArcSectHdr[ i ].entry_count;
		ArcEntry = (ARCENTRY *)malloc( FileCount * sizeof( ARCENTRY ) );
		fread( ArcEntry, sizeof( ARCENTRY ), FileCount, f_arc ); // 3
	fprintf( stderr, "2" );

		// Write all info
		fwrite( &ArcHdr, sizeof( ARCHDR ), 1, f_chs ); // 1
		fwrite( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_chs ); // 2
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs ); // 3, need to change then
	fprintf( stderr, "3" );

		// Calc replacement position
		// SGCC0003_PNG.png
		for( SectId1 = 0; SectId1 < ArcHdr.section_count; SectId1 ++ ) if( !strcmp( ArcSectHdr[ SectId1 ].type, "PNG" ) ) break;
	fprintf( stderr, ".(SectId1=%d)", SectId1 );
		if( SectId1 == ArcHdr.section_count ) return 0; // ERROR02
		for( i = EntryId1 = 0; i < SectId1; i ++ ) EntryId1 += ArcSectHdr[ i ].entry_count;
	fprintf( stderr, "(~%d/%d)", EntryId1, FileCount );
		for( ; EntryId1 < FileCount; EntryId1 ++ ) {
			fprintf( stderr, "\n%d:%s", EntryId1, ArcEntry[ EntryId1 ].filename );
			if( !strcmp( ArcEntry[ EntryId1 ].filename, "SGCC0003" ) ) break;
		}
	fprintf( stderr, "(=%d/%d)", EntryId1, FileCount );
		if( EntryId1 == FileCount ) return 0; // ERROR03
	fprintf( stderr, "4" );

		// SGCC0011_PNG.png
		for( SectId2 = 0; SectId2 < ArcHdr.section_count; SectId2 ++ ) if( !strcmp( ArcSectHdr[ SectId2 ].type, "PNG" ) ) break;
	fprintf( stderr, ".(SectId2=%d)", SectId2 );
		if( SectId2 == ArcHdr.section_count ) return 0; // ERROR02
		for( i = EntryId2 = 0; i < SectId2; i ++ ) EntryId2 += ArcSectHdr[ i ].entry_count;
	fprintf( stderr, "(~%d/%d)", EntryId2, FileCount );
		for( ; EntryId2 < FileCount; EntryId2 ++ ) {
			fprintf( stderr, "\n%d:%s", EntryId2, ArcEntry[ EntryId2 ].filename );
			if( !strcmp( ArcEntry[ EntryId2 ].filename, "SGCC0011" ) ) break;
		}
	fprintf( stderr, "(=%d/%d)", EntryId2, FileCount );
		if( EntryId2 == FileCount ) return 0; // ERROR03
	fprintf( stderr, "4" );

		// Write files
		for( i = 0; i < FileCount; i ++ ) {
			int FileSize;
			if( i == EntryId1 ) { // Need to replace
				f_in = fopen( "Chip_S_arc\\SGCC0003_PNG.png", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else if( i == EntryId2 ) { // Need to replace
				f_in = fopen( "Chip_S_arc\\SGCC0011_PNG.png", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else {
				FileSize = ArcEntry[ i ].length;
				FileDetail = (char *)malloc( FileSize );
				fseek( f_arc, ArcEntry[ i ].offset, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_arc );
			}
			
			fwrite( FileDetail, 1, FileSize, f_chs );
			
			free( FileDetail );
		}
	fprintf( stderr, "5" );
		// ReCalc header info
		for( i = 1; i < FileCount; i ++ )
			ArcEntry[ i ].offset = ArcEntry[ i - 1 ].offset + ArcEntry[ i - 1 ].length;
		fseek( f_chs, sizeof( ARCHDR ) + ArcHdr.section_count * sizeof( ARCSECTHDR ), SEEK_SET );
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs );
		
		
		free( ArcSectHdr );
		free( ArcEntry );
		
		fclose( f_arc );
		fclose( f_chs );
	}
	
	
	
	
	
	
	
	// Chip_T.arc
	{
		int FileCount = 0, i, SectId1, EntryId1, SectId2, EntryId2;
		char *FileDetail;
		FILE *f_arc, *f_chs, *f_in;
		ARCHDR ArcHdr;
		ARCSECTHDR *ArcSectHdr;
		ARCENTRY *ArcEntry;
	fprintf( stderr, "\n>> Chip_T.arc\n" );
		
		f_arc = fopen( "Chip_T.arc", "rb" );
		f_chs = fopen( "Chip_T.chs", "wb" );
		if( f_arc == NULL || f_chs == NULL ) return 0; // ERROR01: fail to open
	fprintf( stderr, "1" );

		// Read all info
		fread( &ArcHdr, sizeof( ARCHDR ), 1, f_arc ); // 1
	fprintf( stderr, "[%d]", ArcHdr.section_count );
		ArcSectHdr = (ARCSECTHDR *)malloc( ArcHdr.section_count * sizeof( ARCSECTHDR ) );
		fread( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_arc ); // 2
		for( i = 0; i < ArcHdr.section_count; i ++ ) FileCount += ArcSectHdr[ i ].entry_count;
		ArcEntry = (ARCENTRY *)malloc( FileCount * sizeof( ARCENTRY ) );
		fread( ArcEntry, sizeof( ARCENTRY ), FileCount, f_arc ); // 3
	fprintf( stderr, "2" );

		// Write all info
		fwrite( &ArcHdr, sizeof( ARCHDR ), 1, f_chs ); // 1
		fwrite( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_chs ); // 2
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs ); // 3, need to change then
	fprintf( stderr, "3" );

		// Calc replacement position
		// SGCC0003_PNG.png
		for( SectId1 = 0; SectId1 < ArcHdr.section_count; SectId1 ++ ) if( !strcmp( ArcSectHdr[ SectId1 ].type, "MSK" ) ) break;
	fprintf( stderr, ".(SectId1=%d)", SectId1 );
		if( SectId1 == ArcHdr.section_count ) return 0; // ERROR02
		for( i = EntryId1 = 0; i < SectId1; i ++ ) EntryId1 += ArcSectHdr[ i ].entry_count;
	fprintf( stderr, "(~%d/%d)", EntryId1, FileCount );
		for( ; EntryId1 < FileCount; EntryId1 ++ ) {
			fprintf( stderr, "\n%d:%s", EntryId1, ArcEntry[ EntryId1 ].filename );
			if( !strcmp( ArcEntry[ EntryId1 ].filename, "T1" ) ) break;
		}
	fprintf( stderr, "(=%d/%d)", EntryId1, FileCount );
		if( EntryId1 == FileCount ) return 0; // ERROR03
	fprintf( stderr, "4" );

		// SGCC0011_PNG.png
		for( SectId2 = 0; SectId2 < ArcHdr.section_count; SectId2 ++ ) if( !strcmp( ArcSectHdr[ SectId2 ].type, "PNG" ) ) break;
	fprintf( stderr, ".(SectId2=%d)", SectId2 );
		if( SectId2 == ArcHdr.section_count ) return 0; // ERROR02
		for( i = EntryId2 = 0; i < SectId2; i ++ ) EntryId2 += ArcSectHdr[ i ].entry_count;
	fprintf( stderr, "(~%d/%d)", EntryId2, FileCount );
		for( ; EntryId2 < FileCount; EntryId2 ++ ) {
			fprintf( stderr, "\n%d:%s", EntryId2, ArcEntry[ EntryId2 ].filename );
			if( !strcmp( ArcEntry[ EntryId2 ].filename, "T1" ) ) break;
		}
	fprintf( stderr, "(=%d/%d)", EntryId2, FileCount );
		if( EntryId2 == FileCount ) return 0; // ERROR03
	fprintf( stderr, "4" );

		// Write files
		for( i = 0; i < FileCount; i ++ ) {
			int FileSize;
			if( i == EntryId1 ) { // Need to replace
				f_in = fopen( "Chip_T_arc\\T1.MSK", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else if( i == EntryId2 ) { // Need to replace
				f_in = fopen( "Chip_T_arc\\T1_PNG.png", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else {
				FileSize = ArcEntry[ i ].length;
				FileDetail = (char *)malloc( FileSize );
				fseek( f_arc, ArcEntry[ i ].offset, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_arc );
			}
			
			fwrite( FileDetail, 1, FileSize, f_chs );
			
			free( FileDetail );
		}
	fprintf( stderr, "5" );
		// ReCalc header info
		for( i = 1; i < FileCount; i ++ )
			ArcEntry[ i ].offset = ArcEntry[ i - 1 ].offset + ArcEntry[ i - 1 ].length;
		fseek( f_chs, sizeof( ARCHDR ) + ArcHdr.section_count * sizeof( ARCSECTHDR ), SEEK_SET );
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs );
		
		
		free( ArcSectHdr );
		free( ArcEntry );
		
		fclose( f_arc );
		fclose( f_chs );
	}


	return 0;
}