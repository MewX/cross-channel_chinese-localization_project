#include "stdafx.h"

/*
//定义链表结点
struct fileInfoNode
{
 struct _finddata64i32_t fileInfo;  //保存文件信息的结构体
 string fileName;
 struct fileInfoNode* left;
};
//把文件信息连接到链表head中
int saveToLink(struct fileInfoNode*& head,   //链表的头结点,引用参量
 const string& fileName,   //IN:文件名(包括路径)
 const struct _finddata64i32_t& fileInfo) //IN:文件信息结构体,引用参量
{
 //建立一个结点
  fileInfoNode* p;
  p=new fileInfoNode;
  p->fileInfo=fileInfo;  //把传入的文件信息复制进结点
  p->fileName=fileName;
  p->left=head;
  head=p;
  return 0;
}
//显示整个查找到的文件的信息
void displayLink(struct fileInfoNode* head)//IN:头结点，值传递参数
{
 while(head!=NULL)
 {
  cout<<"fileName: "<<head->fileName<<endl;
  cout<<"fileSize: "<<dec<<head->fileInfo.size<<"字节"<<endl;
  cout<<"fileAttrib: "<<"0x"<<hex<<head->fileInfo.attrib<<endl;
  cout<<"-------------------------------------------------------------------------------------------"<<endl;
  head=head->left;
 }
}
//把文件信息存储到文件 fileName  中
void saveLinkToFile(struct fileInfoNode* head,string saveFileName,int counter)
{
 ofstream fout;
 //打开文件
 fout.open(saveFileName.c_str());
 if((fout.is_open())==false)
 {
  cout<<"存储文件打开失败！"<<endl;
  exit(-1);
 }
 fout<<"the file number is: "<<counter<<endl;
 fout<<"-------------------------------------------------------------------------------------------------------"<<endl;
 while(head!=NULL)
 {
  fout<<"fileName: "<<head->fileName<<endl;
  fout<<"fileSize: "<<dec<<head->fileInfo.size<<"字节"<<endl;
  fout<<"fileAttrib: "<<"0x"<<hex<<head->fileInfo.attrib<<endl;
  fout<<"-------------------------------------------------------------------------------------------------------"<<endl;
  head=head->left;
 }
 //关闭文件
 fout.close();
}
//
int searchAllFile(string filePath,//IN:文件所在的路径,如：f:example
 int layer,//层次，只有层次为0时，才完成链表中文件信息的显示和存储
   string fileInfoOut)   //IN:存储的文件名
{
 struct _finddata64i32_t fileInfo;//保存文件信息的结构体
 static fileInfoNode* head=NULL; //fileInfoNode链表的头结点,静态存储
 static int counter=0;  //记录文件数目
 long handle;//句柄
 int done;//查找nextfile是否成功
 string fileName=filePath+"\\*.*"; //要搜索的文件名
 //查找第一个文件，返回句柄
 handle=_findfirst64i32(fileName.c_str(),&fileInfo);
 if(handle==-1)
 {
  cout<<"该目录为空!"<<endl;
  //cin.get();
   return -1;
 }
 do
 {
 // cout<<"查找成功"<<endl;
 // cin.get();
 // cout<<fileInfo.name<<endl;
  //如果是文件夹".",或者".."，则进行判断下一个文件
  if((strcmp(fileInfo.name,".")==0)|(strcmp(fileInfo.name,"..")==0))
  {
   //cout<<"丢弃！"<<endl;
   //cin.get();
   continue;
  }
  //如果是文件夹，则进入下一层文件夹搜索
  if((fileInfo.attrib&_A_SUBDIR)==_A_SUBDIR)
  {
 //  cout<<"是文件夹"<<endl;
 //  cin.get();
   string filePathSub=filePath+"\\"+fileInfo.name;
   //递归调用
   searchAllFile(filePathSub,++layer,fileInfoOut);
   layer--;
  }
  //把搜集到的信息连接到文件
  else
  {
//   cout<<"是文件，存储信息!"<<endl;
//   cin.get();
   counter++;
   string fileNameTure=filePath+"\\"+fileInfo.name;
   saveToLink(head,fileNameTure,fileInfo);   //存储到链表中
  }
 }while(!(done=_findnext64i32(handle,&fileInfo)));
 _findclose(handle);
 //layer==时，完成链表的存储
 if(layer==0)
 {
  //显示链表中的内容
   displayLink(head);
  //存储链表中的内容
   saveLinkToFile(head,fileInfoOut,counter);
 }
 return 0;
}*/

//void traversal_dir( char *prefix, char *path);

void CreateFolder( string Name );
void getFileList( string Name, string SaveTo );
void getFileListAndSize( string Name, string SaveTo );

#ifdef CROSSCHANNEL
CrossChannelCrack CC( "Cross Channel Translation Project" );
#endif
#ifdef OTOMEGA
CrossChannelCrack CC( "OtoMega Translation Project" );
#endif

int main( )
{
	CC.RunUI( );

	system( "PAUSE" );
	return 0;
}

void getFileList( string Name, string SaveTo )
{
	if( Name.length( ) > 80 ) {
		cout << "FolderName length cannot be larger than 80!" << endl;
	}
	else {
		char tempName[ 81 ];
		for( unsigned int i = 0; i < Name.length( ); i ++ ) {
			if( Name[ i ] == '\\' || Name[ i ] == '/' || Name[ i ] == ':' || Name[ i ] == '?' ||
					Name[ i ] == '\"' || Name[ i ] == '<' || Name[ i ] == '?' || Name[ i ] == '|' ) {
				cout << "Districted character found!" << endl;
				return;
			}
			tempName[ i ] = Name[ i ];
		}
		tempName[ Name.length( ) ] = '\0';
		if( _access( tempName, 6 ) == -1 ) {
			cout << "Not exsiting folder." << endl;
			return;
		}
		else {
			//traversal_dir( "", tempName );
			
		}
	}
	return;
}

/*void traversal_dir( char *prefix, char *path)
{

	char filename[ 512 ], pathname[ 81 ];
	size_t pathlen = 0;

	char szFind[ MAX_PATH ];
	WIN32_FIND_DATA FindFileData;
	strcpy(szFind,path);
	strcat(szFind,"/*.*");
	HANDLE hFind = ::FindFirstFile( szFind, &FindFileData );
	if( INVALID_HANDLE_VALUE == hFind )
	{
		return;
	}

	while(TRUE)
	{
		if (FindFileData.cFileName[0] != '.') 
		{
			sprintf(filename, "%s/%s", path,FindFileData.cFileName);
			sprintf(pathname, "%s%s", prefix, FindFileData.cFileName);

			//若是目录递归查找
			if(FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
			{
				strcat(pathname, "/");
				traversal_dir(pathname, filename);
			}
			else
			{
				FILE *f = NULL;
				char *buf = NULL;
				if((f=fopen(filename,"r"))==NULL) {
					printf("Error!\n");
					return;
				}
				size_t nFileSize = ftell(f);
				buf = new char[nFileSize+1];
				fread(buf, nFileSize+1, 1,f);
				printf("%s\n", buf);
				delete [ ] buf;
				fclose(f);
			}
		}

		if(!FindNextFile(hFind,&FindFileData)) break;
	}

	FindClose(hFind);
	return;
}
*/