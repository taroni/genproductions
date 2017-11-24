import FWCore.ParameterSet.Config as cms

# link to card:
# https://github.com/cms-sw/genproductions/blob/master/bin/Powheg/production/V2/13TeV/Higgs/

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
                                     args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF30_13TeV_M300_W-0p014_gg_H_quark-mass-effects/v3/gg_H_quark-mass-effects_NNPDF30_13TeV_M300_W-0p014_gg_H_quark-mass-effects.tgz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                                 comEnergy = cms.double(13000.0),
                       	         filterEfficiency = cms.untracked.double(1),
                       	         maxEventsToPrint = cms.untracked.int32(1),
                       	         pythiaHepMCVerbosity = cms.untracked.bool(False),
                       	         pythiaPylistVerbosity = cms.untracked.int32(1),
                       	         PythiaParameters = cms.PSet(
      					 pythia8CommonSettingsBlock,
      					 pythia8CUEP8M1SettingsBlock,
					 pythia8PowhegEmissionVetoSettingsBlock,
                                         processParameters = cms.vstring('POWHEG:nFinal = 1', 
                                                                         'TauDecays:mode = 2', 
                                                                         'TauDecays:tauPolarization = 0', 
                                                                         'TauDecays:tauMother = 25', 
                                                                         '25:m0 = 300.0', 
                                                                         '25:mWidth = 0.042', 
                                                                         '25:addChannel 1 0.1 100 11 -15', 
                                                                         '25:addChannel 1 0.1 100 15 -11', 
                                                                         '25:onMode = off', 
                                                                         '25:onIfMatch 11 15'),
                                         
      					parameterSets = cms.vstring(
                           			'pythia8PowhegEmissionVetoSettings',
                            			'pythia8CommonSettings',
                            			'pythia8CUEP8M1Settings',
                            			'processParameters',
                            			)
      					)
			)

ProductionFilterSequence = cms.Sequence(generator)