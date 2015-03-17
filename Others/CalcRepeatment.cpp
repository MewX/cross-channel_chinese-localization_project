#include <cstdio>
#include <string>
#include <fstream>

using namespace std;

typedef struct {
    char FileName[ 16 ];
    unsigned int idxBeg, idxEnd;
} FileInfo;

int main( )
{
    // global Vars
    fstream AllTextFile;
    unsigned int AllLineCount = 0, FileCount;
    
    // get source folder name
    int option;
    char FolderName[ 256 ];
    printf( "Type import folder: " );
    scanf( "%s", FolderName );
    if( FolderName[ strlen( FolderName ) - 1 ] == '\\' ) FolderName[ strlen( FolderName ) - 1 ] = '\0';
    printf( "Option( 0 ~ FileCount - from this to match ): " );
    scanf( "%d", &option );
    
    
    // make temp folder and get file list using shell
    system( "md temp 2>nul" );
    system( "del temp\\TextFile.lst 2>nul" );
    system( ( (string)"dir " + FolderName + " /A-D-H /B | find /v /c \":\" >> temp\\TextFile.lst" ).c_str( ) );
    system( ( (string)"dir " + FolderName + " /A-D-H /B >> temp\\TextFile.lst" ).c_str( ) );
    
    
    // read all file content, and put them into one text file
    fstream OneTextFile, ListFile;
    char tempText[ 1024 ], tempFileName[ 1024 ];
    
    AllTextFile.open( "temp\\AllText.txt", ios::out | ios::trunc ); // just for write
    ListFile.open( "temp\\TextFile.lst", ios::in );
    
    ListFile >> FileCount;
    for( unsigned int k = 0; k < FileCount; k ++ ) {
        ListFile >> tempFileName;
        OneTextFile.open( ( (string)FolderName + '\\' + tempFileName ).c_str( ), ios::in );
        OneTextFile.clear( );
        
        unsigned int loopCount = 0;
        AllTextFile << ">> " << tempFileName << " <<" << endl; // This is a filename line sig
        while( !OneTextFile.eof( ) ) {
            OneTextFile.getline( tempText, 1024, '\n' );
            if( strlen( tempText ) > 1 ) {
                // purify the string, kick [] {} #### >###
                string cpy = tempText;
                if( strlen( tempText ) > 4 ) {
                    if( tempText[ 0 ] == '#' && tempText[ 1 ] == '#' && tempText[ 2 ] == '#'
                            && ( tempText[ 3 ] == '#' || tempText[ 3 ] == '>' ) ) {
                        strcpy( tempText, cpy.substr( 4, strlen( tempText ) - 4 ).c_str( ) );
                    }
                    else if( tempText[ 0 ] == '[' ) {
                        int temp = 0, len = strlen( tempText );
                        while( temp < len ) {
                            if( tempText[ temp ] == ']' ) break;
                            temp ++;
                        }
                        if( temp != len )
                            strcpy( tempText, cpy.substr( temp + 1, strlen( tempText ) - temp - 1 ).c_str( ) );
                    }
                    else {
                        int temp = 0, len = strlen( tempText ), start, end, mid;
                        for( int j = 0; j < len; j ++ ) { // replace all '{' & ':' & '}'
                            if( tempText[ j ] == '{' ) {
                                start = end = mid = j;
								
								while( mid < len ) {
								    if( tempText[ mid ] == ':' ) break;
									mid ++;
								}
								
                                while( end < len ) {
                                    if( tempText[ end ] == '}' ) break;
                                    end ++;
                                }
								
                                if( end != len && mid < end ) {
                                    strcpy( tempText, cpy.substr( 0, start ).c_str( ) );
									strcat( tempText, cpy.substr( start + 1, mid - start - 1 ).c_str( ) );
                                    strcat( tempText, cpy.substr( end + 1, cpy.length( ) - end - 1 ).c_str( ) );
                                }
                            }
                        }
                    }
                }
                
                // output text
                AllLineCount ++;
                AllTextFile << tempText << endl;
            }
        }
        
        printf( "(%3u/%u) %-12s is ready. (%u)\n", k + 1, FileCount, tempFileName, AllLineCount );
        OneTextFile.close( );
    }
    ListFile.close( );
    AllTextFile.close( );

    
    // save all the text into memory
    string *AllString = new string [ AllLineCount ], tempString;
    FileInfo *fileinfo = new FileInfo [ FileCount ];
    unsigned int idxString = 0, idxFileInfo = 0;
    
    AllTextFile.open( "temp\\AllText.txt", ios::in );
    AllTextFile.clear( );
    while( !AllTextFile.eof( ) ) {
        getline( AllTextFile, tempString );
        if( tempString.length( ) < 2 ) continue;
        
        if( tempString.length( ) > 10 && tempString[ 0 ] == '>' && tempString[ 1 ] == '>'
                && tempString[ tempString.length( ) - 2 ] == '<'
                && tempString[ tempString.length( ) - 1 ] == '<' ) { // FileName info
            strcpy( fileinfo[ idxFileInfo ].FileName, tempString.substr( 3, tempString.length( ) - 6 ).c_str( ) );
            printf( "Registering \"%-12s\" ...\n", fileinfo[ idxFileInfo ].FileName ); // Output the Name
            fileinfo[ idxFileInfo ].idxBeg = fileinfo[ idxFileInfo ].idxEnd = idxString;
            idxFileInfo ++; // Now, idxFileInfo is large than the used one by 1 size
            continue;
        }
        else { // Text
            fileinfo[ idxFileInfo - 1 ].idxEnd = idxString;
            AllString[ idxString ++ ] = tempString; // Copy
        }
    }
    AllTextFile.close( );
    
    
    // make comparation
    fstream ResultFile;
    ResultFile.open( "CalcResult.txt", ios::out | ios::trunc );
	
	ResultFile << "Structure Content:" << endl;
	for( unsigned int i = 0; i < FileCount; i ++ )
	    ResultFile << "FileName: " << fileinfo[ i ].FileName << "; idxBeg: " << fileinfo[ i ].idxBeg << "; idxEnd: " << fileinfo[ i ].idxEnd << endl;
	
	for( idxFileInfo = option; idxFileInfo < FileCount; idxFileInfo ++ ) { // FileInfo loop
	    printf( "Processing match detecting: %-12s ...\n", fileinfo[ idxFileInfo ].FileName );
	    for( unsigned int i = fileinfo[ idxFileInfo ].idxBeg; i <= fileinfo[ idxFileInfo ].idxEnd; i ++ ) { // String in a file loop
		    for( unsigned int idxF = 0; idxF < FileCount; idxF ++ ) { // FileInfo Loop Inner
			    if( idxF == idxFileInfo ) continue;
				for( unsigned int j = fileinfo[ idxF ].idxBeg; j < fileinfo[ idxF ].idxEnd; j ++ ) { // String in a file loop Inner
				    if( AllString[ i ] == AllString[ j ] ) { // matched
					    unsigned int idxOutSave = i, idxInSave = j;
					    while( idxOutSave < fileinfo[ idxFileInfo ].idxEnd && idxInSave < fileinfo[ idxF ].idxEnd
						        && AllString[ ++ idxOutSave ] == AllString[ ++ idxInSave ] ) ;
						if( idxOutSave - i > 5 ) { // ok, I need this
						    char tempResult[ 1024 ];
							sprintf( tempResult, "[ %-12s ] 的 %04d - %04d 行与 [ %-12s ] 的 %04d - %04d 行匹配；", fileinfo[ idxFileInfo ].FileName,
							    i - fileinfo[ idxFileInfo ].idxBeg + 1, idxOutSave - fileinfo[ idxFileInfo ].idxBeg + 1, fileinfo[ idxF ].FileName,
								j - fileinfo[ idxF ].idxBeg + 1, idxInSave - fileinfo[ idxF ].idxBeg + 1 );
							ResultFile << tempResult << endl;
							i = idxOutSave + 1;
							j = idxInSave + 1;
						}
					}
				}
			}
		}	
	}
	ResultFile.close( );
    
    
    // delete garbages
    delete [ ] fileinfo;
    delete [ ] AllString;
    
    system( "pause" );
    return 0;
        
}
