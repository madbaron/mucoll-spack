# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Marlintrkprocessors(CMakePackage, Ilcsoftpackage):
    """A collection of Tracking Relelated Processors Based on MarlinTrk"""

    homepage = "https://github.com/MuonColliderSoft/MarlinTrkProcessors"
    git      = "https://github.com/MuonColliderSoft/MarlinTrkProcessors.git"
    url      = "https://github.com/MuonColliderSoft/MarlinTrkProcessors/archive/refs/tags/v02-14-MC.tar.gz"

    maintainers = ['gianelle', 'pandreetto']

    version('master', branch='master')
    version("2.14",   sha256="618722f38f60a30c4048c97fd0b4ba5f89e81104")
    version("2.13",   sha256="19ec367391e4405616a13418e3f9eb09a3247a73")
    version("2.12",   sha256="61a87aa1ab4b4f66102f27f9861319500edc638a")
    version("2.11",   sha256="4d2dcf0f04d9c02ba8630929e339f742df098760")

    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('dd4hep')
    depends_on('marlintrk')
    depends_on('kitrack')
    depends_on('kitrackmarlin')
    depends_on('gsl')
    depends_on('ddkaltest')
    depends_on('raida')


    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('MARLIN_DLL', self.prefix.lib + "/libMarlinTrkProcessors.so")

    def cmake_args(self):
        return [
            self.define('CMAKE_CXX_STANDARD',
                        self.spec['root'].variants['cxxstd'].value)
        ]
