import FWCore.ParameterSet.Config as cms



externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
                                     args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/powheg/V2/gg_H_quark-mass-effects_NNPDF30_13TeV_M900_W-0p014_gg_H_quark-mass-effects/v2/gg_H_quark-mass-effects_NNPDF30_13TeV_M900_W-0p014_gg_H_quark-mass-effects.tgz '),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
