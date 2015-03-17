/* Copyright (C) 2012 Connor Olding
 *
 * This program is licensed under the terms of the MIT License, and
 * is distributed without any warranty.  You should have received a
 * copy of the license along with this program; see the file LICENSE.
 */
#define ulong unsigned long

enum { CRC_TABLE_SIZE = 0x100 };

void crc_fill_table(ulong *table, int big, ulong polynomial);
void crc_be_cycle(ulong *table, ulong *remainder, char c);
void crc_le_cycle(ulong *table, ulong *remainder, char c);
ulong crc_reflect(ulong input);

#undef ulong
