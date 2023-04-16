
# python wrapper for package measure_dist within overall package measure_dist
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=measure_dist -vm=python3 .

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
    import collections.abc as _collections_abc
except ImportError:
    _collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _measure_dist
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from measure_dist import measure_dist
# and then refer to everything using measure_dist. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for slice [][]float64
class Slice_Slice_float64(go.GoClass):
    """"""
    def __init__(self, *args, **kwargs):
        """
        handle=A Go-side object is always initialized with an explicit handle=arg
        otherwise parameter is a python list that we copy from
        """
        self.index = 0
        if len(kwargs) == 1 and 'handle' in kwargs:
            self.handle = kwargs['handle']
            _measure_dist.IncRef(self.handle)
        elif len(args) == 1 and isinstance(args[0], go.GoClass):
            self.handle = args[0].handle
            _measure_dist.IncRef(self.handle)
        else:
            self.handle = _measure_dist.Slice_Slice_float64_CTor()
            _measure_dist.IncRef(self.handle)
            if len(args) > 0:
                if not isinstance(args[0], _collections_abc.Iterable):
                    raise TypeError('Slice_Slice_float64.__init__ takes a sequence as argument')
                for elt in args[0]:
                    self.append(elt)
    def __del__(self):
        _measure_dist.DecRef(self.handle)
    def __str__(self):
        s = 'measure_dist.Slice_Slice_float64 len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
        if len(self) < 120:
            s += ', '.join(map(str, self)) + ']'
        return s
    def __repr__(self):
        return 'measure_dist.Slice_Slice_float64([' + ', '.join(map(str, self)) + '])'
    def __len__(self):
        return _measure_dist.Slice_Slice_float64_len(self.handle)
    def __getitem__(self, key):
        if isinstance(key, slice):
            if key.step == None or key.step == 1:
                st = key.start
                ed = key.stop
                if st == None:
                    st = 0
                if ed == None:
                    ed = _measure_dist.Slice_Slice_float64_len(self.handle)
                return Slice_Slice_float64(handle=_measure_dist.Slice_Slice_float64_subslice(self.handle, st, ed))
            return [self[ii] for ii in range(*key.indices(len(self)))]
        elif isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError('slice index out of range')
            return go.Slice_float64(handle=_measure_dist.Slice_Slice_float64_elem(self.handle, key))
        else:
            raise TypeError('slice index invalid type')
    def __setitem__(self, idx, value):
        if idx < 0:
            idx += len(self)
        if idx < len(self):
            _measure_dist.Slice_Slice_float64_set(self.handle, idx, value.handle)
            return
        raise IndexError('slice index out of range')
    def __iadd__(self, value):
        if not isinstance(value, _collections_abc.Iterable):
            raise TypeError('Slice_Slice_float64.__iadd__ takes a sequence as argument')
        for elt in value:
            self.append(elt)
        return self
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(self):
            rv = _measure_dist.Slice_Slice_float64_elem(self.handle, self.index)
            self.index = self.index + 1
            return rv
        raise StopIteration
    def append(self, value):
        go_val = go.Slice_float64(value)
        _measure_dist.Slice_Slice_float64_append(self.handle, go_val.handle)
    def copy(self, src):
        """ copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
        mx = min(len(self), len(src))
        for i in range(mx):
            self[i] = src[i]


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def calculate_iou(boxA, boxB):
    """CalculateIOU([]int boxA, []int boxB) float"""
    go_boxA = go.Slice_int(boxA)
    go_boxB = go.Slice_int(boxB)
    return _measure_dist.measure_dist_CalculateIOU(go_boxA.handle, go_boxB.handle)
def enlarge_area(area, margin, imageWidth, imageHeight):
    """EnlargeArea([]int area, int margin, int imageWidth, int imageHeight) []int"""
    go_area = go.Slice_int(area)
    return go.Slice_int(handle=_measure_dist.measure_dist_EnlargeArea(go_area.handle, margin, imageWidth, imageHeight))
def is_inside_area(objectBox, area):
    """IsInsideArea([]int objectBox, []int area) bool"""
    go_objectBox = go.Slice_int(objectBox)
    go_area = go.Slice_int(area)
    return _measure_dist.measure_dist_IsInsideArea(go_objectBox.handle, go_area.handle)
def merge_boxes(box1, box2):
    """MergeBoxes([]int box1, []int box2) []int"""
    go_box1 = go.Slice_int(box1)
    go_box2 = go.Slice_int(box2)
    return go.Slice_int(handle=_measure_dist.measure_dist_MergeBoxes(go_box1.handle, go_box2.handle))
def xywh_to_xyxy(iCrop):
    """XywhToXyxy([]int iCrop) []int"""
    go_iCrop = go.Slice_int(iCrop)
    return go.Slice_int(handle=_measure_dist.measure_dist_XywhToXyxy(go_iCrop.handle))
def calculate_area(box):
    """CalculateArea([]int box) int"""
    go_box = go.Slice_int(box)
    return _measure_dist.measure_dist_CalculateArea(go_box.handle)
def coordinate_to_azimuth(coordinate):
    """CoordinateToAzimuth([]float coordinate) float"""
    go_coordinate = go.Slice_float64(coordinate)
    return _measure_dist.measure_dist_CoordinateToAzimuth(go_coordinate.handle)
def three_p_center_point(mesh):
    """ThreePCenterPoint([][]float mesh) []float"""
    go_mesh = Slice_Slice_float64(mesh.tolist())
    return go.Slice_float64(handle=_measure_dist.measure_dist_ThreePCenterPoint(go_mesh.handle))
def two_p_center_point(mesh):
    """TwoPCenterPoint([][]float mesh) []float"""
    go_mesh = Slice_Slice_float64(mesh.tolist())
    return go.Slice_float64(handle=_measure_dist.measure_dist_TwoPCenterPoint(go_mesh.handle))


