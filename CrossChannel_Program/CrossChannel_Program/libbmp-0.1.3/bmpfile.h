/**
 * @file bmpfile.h
 * @brief The BMP library header
 *
 * libbmp - BMP library
 * Copyright (C) 2009 lidaibin(超越无限)
 * mail: lidaibin@gmail.com
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 *
 * $Id$
 */

#ifndef __bmpfile_h__
#define __bmpfile_h__

#pragma pack( 1 ) // cancel align

#ifdef __cplusplus
#define BMP_BEGIN_DECLS extern "C" {
#define BMP_END_DECLS }
#else
#define BMP_BEGIN_DECLS
#define BMP_END_DECLS
#endif

BMP_BEGIN_DECLS

//#ifndef bool
//typedef int bool;
//#define FALSE (0)
//#define TRUE !FALSE
//#endif

#ifndef uint8_t
typedef unsigned char uint8_t;
#endif

#ifndef uint16_t
typedef unsigned short uint16_t;
#endif

#ifndef uint32_t
typedef unsigned int uint32_t;
#endif

//typedef enum {
//  BI_RGB = 0,
//  BI_RLE8,
//  BI_RLE4,
//  BI_BITFIELDS,
//  BI_JPEG,
//  BI_PNG,
//} bmp_compression_method_t;

typedef struct {
  uint8_t blue;
  uint8_t green;
  uint8_t red;
  uint8_t alpha;
} rgb_pixel_t;

typedef struct {
  uint8_t magic[ 2 ]; /* the magic number used to identify the BMP file:
			 0x42 0x4D (Hex code points for B and M).
			 The following entries are possible:
			 BM - Windows 3.1x, 95, NT, ... etc
			 BA - OS/2 Bitmap Array
			 CI - OS/2 Color Icon
			 CP - OS/2 Color Pointer
			 IC - OS/2 Icon
			 PT - OS/2 Pointer. */
  uint32_t filesz;    /* the size of the BMP file in bytes */
  uint16_t creator1;  /* reserved. */
  uint16_t creator2;  /* reserved. */
  uint32_t offset;    /* the offset, i.e. starting address,
			 of the byte where the bitmap data can be found. */
} bmp_header_t;

typedef struct {
  uint32_t header_sz;     /* the size of this header (40 bytes) */
  uint32_t width;         /* the bitmap width in pixels */
  uint32_t height;        /* the bitmap height in pixels */
  uint16_t nplanes;       /* the number of color planes being used.
			     Must be set to 1. */
  uint16_t depth;         /* the number of bits per pixel,
			     which is the color depth of the image.
			     Typical values are 1, 4, 8, 16, 24 and 32. */
  uint32_t compress_type; /* the compression method being used.
			     See also bmp_compression_method_t. */
  uint32_t bmp_bytesz;    /* the image size. This is the size of the raw bitmap
			     data (see below), and should not be confused
			     with the file size. */
  uint32_t hres;          /* the horizontal resolution of the image.
			     (pixel per meter) */
  uint32_t vres;          /* the vertical resolution of the image.
			     (pixel per meter) */
  uint32_t ncolors;       /* the number of colors in the color palette,
			     or 0 to default to 2<sup><i>n</i></sup>. */
  uint32_t nimpcolors;    /* the number of important colors used,
			     or 0 when every color is important;
			     generally ignored. */
} bmp_dib_v3_header_t;

typedef struct _bmpfile bmpfile_t;

bmpfile_t *bmp_create(uint32_t width, uint32_t height, uint32_t depth);
//bmpfile_t *bmp_create_from_file(const char *filename); /* This function is written by MewCatcher */
void bmp_destroy(bmpfile_t *bmp);

bmp_header_t bmp_get_header(bmpfile_t *bmp);
bmp_dib_v3_header_t bmp_get_dib(bmpfile_t *bmp);

uint32_t bmp_get_width(bmpfile_t *bmp);
uint32_t bmp_get_height(bmpfile_t *bmp);
uint32_t bmp_get_depth(bmpfile_t *bmp);

uint32_t bmp_get_dpi_x(bmpfile_t *bmp);
uint32_t bmp_get_dpi_y(bmpfile_t *bmp);
void bmp_set_dpi(bmpfile_t *bmp, uint32_t x, uint32_t y);

rgb_pixel_t *bmp_get_pixel(bmpfile_t *bmp, uint32_t x, uint32_t y);
bool bmp_set_pixel(bmpfile_t *bmp, uint32_t x, uint32_t y, rgb_pixel_t pixel);

bool bmp_save(bmpfile_t *bmp, const char *filename);

BMP_END_DECLS

#endif /* __bmpfile_h__ */
