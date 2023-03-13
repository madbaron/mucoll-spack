# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.k4.key4hep_stack import Ilcsoftpackage


class Lcgeo(CMakePackage, Ilcsoftpackage):
    """DD4hep geometry models for future colliders."""

    homepage = "https://github.com/MuonColliderSoft/lcgeo"
    git      = "https://github.com/MuonColliderSoft/lcgeo.git"
    url      = "https://github.com/MuonColliderSoft/lcgeo/archive/refs/tags/v00-17-MC.tar.gz"

    generator = 'Ninja'

    maintainers = ['gianelle', 'pandreetto']

    version('master',  branch='master')
    version("0.17",    sha256="15933f25cda16a312bc0413e896401b65702b94f")
    version("0.16.08", sha256="831f3363dff6519719686e27cc9a05cf60926734")
    version("0.16.07", sha256="1ca26fe531671a34e6a0a41cc625638b4f065fbf")
    version("0.16.06", sha256="975bf03213415a8109b26f0d05d1a402729778ce")

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('lcio')
    depends_on('dd4hep')
    depends_on('lcio')
    depends_on('boost')
    depends_on('root')
    depends_on('python', type='build')
    depends_on('ninja', type='build')


    def cmake_args(self):
        args = []  
        args.append(self.define_from_variant('CMAKE_CXX_STANDARD', 'cxxstd'))
        args.append(self.define('BUILD_TESTING', self.run_tests))
        return args


    @run_after('install')
    def install_compact(self):
        install_tree('CaloTB', self.prefix.share.lcgeo.compact.CaloTB)
        install_tree('CLIC', self.prefix.share.lcgeo.compact.CLIC)
        install_tree('FCalTB', self.prefix.share.lcgeo.compact.FCalTB)
        install_tree('FCCee', self.prefix.share.lcgeo.compact.FCCee)
        install_tree('fieldmaps', self.prefix.share.lcgeo.compact.fieldmaps)
        install_tree('ILD', self.prefix.share.lcgeo.compact.ILD)
        install_tree('SiD', self.prefix.share.lcgeo.compact.Sid)

    def setup_run_environment(self, env):
        env.set('LCGEO', self.prefix.share.lcgeo.compact)
        env.set('lcgeo_DIR', self.prefix.share.lcgeo.compact)

    def setup_build_environment(self, env):
        env.set('LCGEO', self.prefix.share.lcgeo.compact)
        env.set('lcgeo_DIR', self.prefix.share.lcgeo.compact)
        env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib')
        env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib64')
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    def setup_dependent_build_environment(self, spack_env, dependent_spec):
        spack_env.set('LCGEO', self.prefix.share.lcgeo.compact)
        spack_env.set('lcgeo_DIR', self.prefix.share.lcgeo.compact)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix.lib)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcgeo'].prefix.lib64)
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib')
        spack_env.prepend_path("LD_LIBRARY_PATH", self.spec['lcio'].prefix + '/lib64')

    # dd4hep tests need to run after install step:
    # disable the usual check
    def check(self):
        pass

    # instead add custom check step that runs after installation
    @run_after('install')
    def install_check(self):
        print(self)
        with working_dir(self.build_directory):
            if self.run_tests:
                ninja('test')

