//////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2008-2011, Image Engine Design Inc. All rights reserved.
//
//  Copyright 2010 Dr D Studios Pty Limited (ACN 127 184 954) (Dr. D Studios),
//  its affiliates and/or its licensors.
//
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//
//     * Neither the name of Image Engine Design nor the names of any
//       other contributors to this software may be used to endorse or
//       promote products derived from this software without specific prior
//       written permission.
//
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////

#ifndef IECOREMAYA_FROMMAYASKINCLUSTERWEIGHTSCONVERTER_H
#define IECOREMAYA_FROMMAYASKINCLUSTERWEIGHTSCONVERTER_H

#include "IECoreMaya/FromMayaObjectConverter.h"


namespace IECoreMaya
{

IE_CORE_FORWARDDECLARE( FromMayaSkinClusterWeightsConverter );

/// The FromMayaSkinClusterWeightsConverter converts skinCluster weigths from maya skinCluster nodes
class IECOREMAYA_API FromMayaSkinClusterWeightsConverter : public FromMayaObjectConverter
{

	public :

		FromMayaSkinClusterWeightsConverter( const MObject &object );

		IE_CORE_DECLARERUNTIMETYPEDEXTENSION( FromMayaSkinClusterWeightsConverter, FromMayaSkinClusterWeightsConverterTypeId, FromMayaObjectConverter );

	protected :

		virtual IECore::ObjectPtr doConversion( const MObject &object, IECore::ConstCompoundObjectPtr operands ) const;

	private :

		static FromMayaObjectConverterDescription<FromMayaSkinClusterWeightsConverter> m_description;

};

IE_CORE_DECLAREPTR( FromMayaSkinClusterWeightsConverter );

} // namespace IECoreMaya

#endif // IECOREMAYA_FROMMAYASKINCLUSTERWEIGHTSCONVERTER_H
