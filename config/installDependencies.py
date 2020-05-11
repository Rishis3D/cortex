#!/usr/bin/env python

##########################################################################
#
#  Copyright (c) 2017, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import os
import re
import sys
import glob
import shutil
import urllib
import argparse
import hashlib

# Determine default archive URL. We use the packages for Gaffer, since we
# know they also include everything needed by Cortex, and we don't want to
# maintain multiple packages (one is enough of a pain already).

platform = { "darwin": "osx", "win32": "windows" }.get( sys.platform, "linux" )
if platform == "osx" or platform == "linux" :
	defaultURL = "https://github.com/GafferHQ/dependencies/releases/download/0.54.2.0/gafferDependencies-0.54.2.0-" + platform + ".tar.gz"
else :
	defaultURL = "https://github.com/hypothetical-inc/gafferDependencies/releases/download/0.54.1.0/gafferDependencies-0.54.1.0-windows-msvc2017.zip"

# Parse command line arguments.

parser = argparse.ArgumentParser()

parser.add_argument(
	"--archiveURL",
	help = "The URL to download the dependencies archive from.",
	default = defaultURL,
)

parser.add_argument(
	"--dependenciesDir",
	help = "The directory to unpack the dependencies into.",
	default = "dependencies",
)

parser.add_argument(
	"--outputFormat",
	help = "A format string that specifies the output printed "
		"by this script. May contain {archiveURL} and {archiveDigest} "
		"tokens that will be substituted appropriately.",
	default = "",
)

args = parser.parse_args()

# Download and unpack the archive.

sys.stderr.write( "Downloading dependencies \"%s\"\n" % args.archiveURL )
archiveFileName, headers = urllib.urlretrieve( args.archiveURL )

os.makedirs( args.dependenciesDir )
if platform == "osx" or platform == "linux" :
	os.system( "tar xf %s -C %s --strip-components=1" % ( archiveFileName, args.dependenciesDir ) )
else :
	os.system( "7z x %s -o%s -aoa -y" % ( archiveFileName, args.dependenciesDir ) )

# Remove all Cortex related files from the package, so there is no conflict
# with the files generated by our build.

for pattern in [
	"include/IECore*",
	"lib/libIECore*",
	"python/IECore*",
	"arnold",
	"renderMan",
	"procedurals",
] :
	for f in glob.glob( os.path.join( args.dependenciesDir, pattern ) ) :
		if os.path.isdir( f ) :
			shutil.rmtree( f )
		else :
			os.remove( f )

# Tell the world

if args.outputFormat :

	md5 = hashlib.md5()
	with open( archiveFileName ) as f :
		md5.update( f.read() )

	print(
		args.outputFormat.format(
			archiveURL = args.archiveURL,
			archiveDigest = md5.hexdigest()
		)
	)