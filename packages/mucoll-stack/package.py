import os

# import common methods for use in recipe from mucoll_utils.py
# (so other recipe can import from spack.pkg.mucoll.mucoll_stack)
# (which is the most convenient way to make that code available
#  without creation of a new module
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from mucoll_utils import *

from spack.pkg.k4.key4hep_stack import Key4hepPackage, install_setup_script


class MucollStack(BundlePackage, Key4hepPackage):
    """Bundle package to install Ilcsoft"""
    
    homepage = 'https://github.com/MuonColliderSoft'

    ##################### versions ########################
    #######################################################
    ###  nightly build
    # to install latest the version of every dependency
    # should use `environments/mucoll-common/packages.yaml`
    version('master')

    ### stable build
    # to install exact specified version for every dependecy
    # should use `environments/mucoll-release/packages.yaml`
    version('2.8')

    # this bundle package installs a custom setup script, so
    # need to add the install phase 
    # (normally doesn't exist for a bundle package)
    phases = ['install']

    variant('devtools', default=True,
            description='add tools necessary for software development to the stack')
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))


    ############################### Key4hep ###############
    #######################################################
    depends_on('whizard +lcio +openloops')
    depends_on('k4lcioreader')
    depends_on('k4simdelphes')
    depends_on('delphes')


    ############################### ILCSoft ###############
    #######################################################
    depends_on('aidatt')
    depends_on('raida')
    depends_on('sio')
    depends_on('ced')
    depends_on('cedviewer')
    depends_on('garlic')
    depends_on('k4marlinwrapper')
    depends_on('generalbrokenlines')
    depends_on('gear')
    depends_on('ilcutil')
    depends_on('lcfiplus')
    depends_on('lcfivertex')
    depends_on('marlin')
    depends_on('marlinutil')
    depends_on('marlindd4hep')
    depends_on('marlinreco')
    depends_on('marlinfastjet')
    depends_on('marlinkinfit')
    depends_on('marlinkinfitprocessors')
    depends_on('marlintrk')
    depends_on('kaldet')
    depends_on('ddkaltest')
    depends_on('kitrackmarlin')
    depends_on('kaltest')
    depends_on('kitrack')
    depends_on('fcalclusterer')
    depends_on('pandoraanalysis')
    depends_on('pandorapfa')
    depends_on('clicperformance')


    ############## modified ILCSoft packages ##############
    #######################################################
    depends_on('lcio')
    depends_on('lcgeo')
    depends_on('lctuple')
    depends_on('overlay')
    depends_on('marlintrkprocessors')
    depends_on('forwardtracking')
    depends_on('conformaltracking')
    depends_on('ddmarlinpandora')

    ############ custom Muon Collider packages ############
    #######################################################
    depends_on('actstracking')
    depends_on('muoncvxddigitiser')


    ##################### developer tools #################
    #######################################################
    with when('+devtools'):
        depends_on('cmake')
        depends_on('ninja')

    ##################### conflicts #######################
    #######################################################
    conflicts("%gcc@8.3.1",
              msg="There are known issues with compilers from redhat's devtoolsets" \
              "which are therefore not supported." \
              "See https://root-forum.cern.ch/t/devtoolset-gcc-toolset-compatibility/38286")

    def setup_run_environment(self, spack_env):
        # set locale to avoid certain issues with xerces-c
        # (see https://github.com/key4hep/key4hep-spack/issues/170)
        spack_env.set("LC_ALL", "C")
        spack_env.set('MUCOLL_STACK', os.path.join(self.spec.prefix, 'setup.sh'))

    def install(self, spec, prefix):
        return install_setup_script(self, spec, prefix, 'MUCOLL_LATEST_SETUP_PATH')
