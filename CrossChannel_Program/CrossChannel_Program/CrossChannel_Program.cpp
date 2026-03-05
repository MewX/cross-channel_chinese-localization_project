#include "stdafx.h"

#ifdef CROSSCHANNEL
CrossChannelCrack CC( "Cross Channel Translation Project" );
#endif
#ifdef OTOMEGA
CrossChannelCrack CC( "OtoMega Translation Project" );
#endif
#ifdef IOREVISION
CrossChannelCrack CC("I/O Revision II Translation Project");
#endif

int main( )
{
	CC.__3_Decrypt("source");
	//CC.__1_Unpack2("Rio.arc","source");
	//CC.__4_Encrypt("source","encrypt");
	//CC.__2_Pack("Rio.arc", "encrypt\\WSC_ENC");
	return 0;
}
