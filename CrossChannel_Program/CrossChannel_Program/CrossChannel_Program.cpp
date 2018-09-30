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
	CC.RunUI( );

	system( "PAUSE" );
	return 0;
}
