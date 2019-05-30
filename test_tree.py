from tree import (partition_by, partition_entropy_by, best_partition_entropy, build_tree_id3)
from pytest import approx
from math import log2

def test_partition_by():
    # input is list of (x^hat, y), which variable (by index) to cut on, and the threshold
    assert partition_by([([0], 1), ([2], 2)], 0, 1) == ([([0], 1)], [([2], 2)])
    assert partition_by([([0,1], 1), ([2,1], 2)], 0, 1) == ([([0,1], 1)], [([2,1], 2)])
    assert partition_by([([0,1], 1), ([2,0.], 2)], 1, 0.5) == ([([2,0], 2)], [([0,1], 1)])
    assert partition_by([([0,1], 1), ([2,0.], 2)], 1, 0.5) == ( [([2,0], 2)] , [([0,1], 1)] )

def test_partition_entropy_by():
    # as for partition_by, but also calculates the partition entropy of the resulting split
    assert partition_entropy_by([([0], 1), ([2], 2)], 0, 1) == (([([0], 1)], [([2], 2)]), 0)

def test_best_partition_entropy():
    # returns the (attr. index, theshold), partition_entropy of the
    # cut that gives the best (lowest) resulting partition entropy
    # potential cut values chosen from the input datapoints
    assert best_partition_entropy([([0], 1), ([2], 2)]) in [((0, 0), 0), (0, 2), 0]
    assert best_partition_entropy([([0, 2], 1), ([2, 2], 2)]) in [((0, 0), 0), (0, 2), 0]

def test_build_tree_id3():
    inputs = [((0.29216567898986456, 0.5351554082642969), 1), ((0.22986846876784384, 0.37369827663748245), 1), ((0.5926366737546702, 0.8953442360305133), 1), ((0.07920494156650915, 0.9527062799015618), 1), ((0.1325393784407547, 0.9616459026020442), 1), ((0.8427165440886971, 0.9795998368484086), 1), ((0.15837216917568608, 0.822298542384515), 1), ((0.519216730492731, 0.5538784320277804), 1), ((0.35608237925243136, 0.6033833681339001), 1), ((0.3130816872120834, 0.8353071593292579), 1), ((0.17764152105816755, 0.6345414241684852), 1), ((0.4570799911452954, 0.9566585276271388), 1), ((0.6518715807835593, 0.6542997841090329), 1), ((0.06450727283476698, 0.3102435519995982), 1), ((0.3648037909289017, 0.6916274511594128), 1), ((0.8195144841295547, 0.9329085109586034), 1), ((0.5148508455830145, 0.7421541663754873), 1), ((0.10957320734132747, 0.5831229316932539), 1), ((0.5019962965375173, 0.977199635735707), 1), ((0.5288180916521509, 0.8977935632552697), 1), ((0.04144352547902308, 0.10258979237312993), 1), ((0.07848845732919407, 0.7031281314053823), 1), ((0.3443234126757104, 0.8764645970839912), 1), ((0.1590141330726179, 0.8378079225204352), 1), ((0.05293548421357652, 0.7308997348374037), 1), ((0.21117229371152768, 0.8135092344382742), 1), ((0.03752609937058937, 0.712503029150964), 1), ((0.007908374025138443, 0.16722145212702233), 1), ((0.6012541013240673, 0.42379558483034907), 0), ((0.9340005807823545, 0.3100909893974787), 0), ((0.994786281704111, 0.41208054231532076), 0), ((0.7247469454347405, 0.06348369697016698), 0), ((0.8642065894866702, 0.09554612904005155), 0), ((0.9352951431380345, 0.8014698022021406), 0), ((0.6847874784960319, 0.13639537396338564), 0), ((0.8128833436207231, 0.2421231472821621), 0), ((0.3294127945129024, 0.25714063045451807), 0), ((0.2857069667365839, 0.16724650637524796), 0), ((0.5445434145849303, 0.38630133216407725), 0), ((0.5659350766796961, 0.06539871539324349), 0), ((0.8003725539037331, 0.4944577719257519), 0), ((0.7113425712678376, 0.5298559996206679), 0), ((0.8924593175166294, 0.015351941595016516), 0), ((0.9232660385209598, 0.053024073164343766), 0), ((0.9586484679957462, 0.7969774916260804), 0), ((0.46248323431408234, 0.1292508010586112), 0), ((0.8316846056103339, 0.32225367124815296), 0), ((0.8098640975075796, 0.3784094813606841), 0), ((0.817466529659476, 0.1969911361044615), 0), ((0.19072950701141633, 0.17146613935308785), 0)]
    tr = build_tree_id3(inputs, 100)
    assert tr == ([(1, approx(0.5298559996206679)), [(0, approx(0.22986846876784384)), [(0, approx(0.06450727283476698)), 1, [(0, approx(0.19072950701141633)), 0, 1]], 0], [(0, approx(0.8427165440886971)), 1, 0]])
