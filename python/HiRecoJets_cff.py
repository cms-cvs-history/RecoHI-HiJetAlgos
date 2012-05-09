import FWCore.ParameterSet.Config as cms

from RecoJets.Configuration.CaloTowersRec_cff import *

## Default Parameter Sets
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoHI.HiJetAlgos.HiCaloJetParameters_cff import *

## Calo Towers
CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz')
)

caloTowers = cms.EDProducer("CaloTowerCandidateCreator",
    src = cms.InputTag("towerMaker"),
    e = cms.double(0.0),
    verbose = cms.untracked.int32(0),
    pt = cms.double(0.0),
    minimumE = cms.double(0.0),
    minimumEt = cms.double(0.0),
    et = cms.double(0.0)
)

## Iterative Cone
iterativeConePu5CaloJets = cms.EDProducer(
    "FastjetJetProducer",
    HiCaloJetParameters,
    AnomalousCellParameters,
    MultipleAlgoIteratorBlock,
    jetAlgorithm = cms.string("IterativeCone"),
    rParam       = cms.double(0.5)
    )
iterativeConePu5CaloJets.radiusPU = 0.5

iterativeConePu7CaloJets = cms.EDProducer(
    "FastjetJetProducer",
    HiCaloJetParameters,
    AnomalousCellParameters,
    MultipleAlgoIteratorBlock,
    jetAlgorithm = cms.string("IterativeCone"),
    rParam       = cms.double(0.7)
    )
iterativeConePu7CaloJets.radiusPU = 0.7

## kT
ktPu4CaloJets = cms.EDProducer(
    "FastjetJetProducer",
    HiCaloJetParameters,
    AnomalousCellParameters,
    MultipleAlgoIteratorBlock,
    jetAlgorithm = cms.string("Kt"),
    rParam       = cms.double(0.4)
    )
ktPu4CaloJets.radiusPU = 0.5

ktPu6CaloJets = cms.EDProducer(
    "FastjetJetProducer",
    HiCaloJetParameters,
    AnomalousCellParameters,
    MultipleAlgoIteratorBlock,
    jetAlgorithm = cms.string("Kt"),
    rParam       = cms.double(0.6)
    )
ktPu6CaloJets.radiusPU = 0.7

## anti-kT
akPu5CaloJets = cms.EDProducer(
    "FastjetJetProducer",
    HiCaloJetParameters,
    AnomalousCellParameters,
    MultipleAlgoIteratorBlock,
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.5)
    )
akPu5CaloJets.radiusPU = 0.5

akPu7CaloJets = cms.EDProducer(
    "FastjetJetProducer",
    HiCaloJetParameters,
    AnomalousCellParameters,
    MultipleAlgoIteratorBlock,
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.7)
    )
akPu7CaloJets.radiusPU = 0.7

## Algos without offset pileup correction
ic5CaloJets = iterativeConePu5CaloJets.clone()
ic5CaloJets.doRhoFastjet = True
ic5CaloJets.doPUOffsetCorr = False

ic7CaloJets = iterativeConePu7CaloJets.clone()
ic7CaloJets.doRhoFastjet = True
ic7CaloJets.doPUOffsetCorr = False

ak5CaloJets = akPu5CaloJets.clone()
ak5CaloJets.doRhoFastjet = True
ak5CaloJets.doPUOffsetCorr = False

ak7CaloJets = akPu7CaloJets.clone()
ak7CaloJets.doRhoFastjet = True
ak7CaloJets.doPUOffsetCorr = False

kt4CaloJets = ktPu4CaloJets.clone()
kt4CaloJets.doRhoFastjet = True
kt4CaloJets.doPUOffsetCorr = False

kt6CaloJets = ktPu6CaloJets.clone()
kt6CaloJets.doRhoFastjet = True
kt6CaloJets.doPUOffsetCorr = False

## Default Sequence
hiRecoJets = cms.Sequence(caloTowersRec*caloTowers*iterativeConePu5CaloJets)

## Extended Sequence
hiRecoAllJets = cms.Sequence(caloTowersRec*caloTowers*iterativeConePu5CaloJets+iterativeConePu7CaloJets+ic5CaloJets+ic7CaloJets+akPu5CaloJets+akPu7CaloJets+ak5CaloJets+ak7CaloJets + ktPu4CaloJets + ktPu6CaloJets +  kt4CaloJets + kt6CaloJets)

### Extra extended algos & sequence
akPu6PFJets = akPu3PFJets.clone(rParam = 0.6)
akPu6CaloJets = akPu3CaloJets.clone(rParam = 0.6)
akPu4PFJets = akPu3PFJets.clone(rParam = 0.4)
akPu4CaloJets = akPu3CaloJets.clone(rParam = 0.4)
akPu2PFJets = akPu3PFJets.clone(rParam = 0.2)
akPu2CaloJets = akPu3CaloJets.clone(rParam = 0.2)
akPu1PFJets = akPu3PFJets.clone(rParam = 0.1)
akPu1CaloJets = akPu3CaloJets.clone(rParam = 0.1)

iterativeCone5CaloJets = iterativeConePu5CaloJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak6PFJets = akPu6PFJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak6CaloJets = akPu6CaloJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak5PFJets = akPu5PFJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak5CaloJets = akPu5CaloJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak4PFJets = akPu4PFJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak4CaloJets = akPu4CaloJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak3PFJets = akPu3PFJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak3CaloJets = akPu3CaloJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak2PFJets = akPu2PFJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak2CaloJets = akPu2CaloJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak1PFJets = akPu1PFJets.clone(doPUOffsetCorr = False, jetPtMin = 1)
ak1CaloJets = akPu1CaloJets.clone(doPUOffsetCorr = False, jetPtMin = 1)

recoAk1to6 = cms.Sequence( akPu1PFJets * akPu2PFJets *akPu3PFJets * akPu4PFJets * akPu5PFJets * akPu6PFJets *
                           ak1PFJets * ak2PFJets *ak3PFJets * ak4PFJets * ak5PFJets * ak6PFJets *
                           akPu1CaloJets * akPu2CaloJets *akPu3CaloJets * akPu4CaloJets * akPu5CaloJets * akPu6CaloJets *
                           ak1CaloJets * ak2CaloJets *ak3CaloJets * ak4CaloJets * ak5CaloJets * ak6CaloJets
                           )











