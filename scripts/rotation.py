import argparse
import vtk

def rotation(in_file, out_file, angle, x, y, z):
      '''Rotate a vtp or vtk file by ${angle}° along x, y or z axis.'''
      if in_file[-3:] == 'vtp':
            reader = vtk.vtkXMLPolyDataReader()
            writer = vtk.vtkXMLPolyDataWriter()
      elif in_file[-3:] == 'vtk':
            reader = vtk.vtkPolyDataReader()
            writer = vtk.vtkPolyDataWriter()
      else :
            raise Exception("Unrecognized input file. Must be vtp or vtk.")
      reader.SetFileName(in_file)
      reader.Update()
      translation = vtk.vtkTransform()
      translation.RotateWXYZ(angle, x, y, z)
      transformFilter = vtk.vtkTransformPolyDataFilter()
      transformFilter.SetInputConnection(reader.GetOutputPort())
      transformFilter.SetTransform(translation)
      transformFilter.Update()
      writer.SetFileName(out_file)
      writer.SetInputConnection(transformFilter.GetOutputPort())
      if in_file[-3:] == 'vtk':
            writer.SetFileVersion(42) #the constant 42 is defined in IO/Legacy/vtkDataWriter.h (c++ code), it corresponds to VTK_LEGACY_READER_VERSION_4_2
      writer.Update()
      writer.Write()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Rotation", description="This program rotates a vtp or vtk track file around a desired axis and by a desired angle. By default, it performs a rotation by 180° around z axis, enabling to move from RAS orientation convention to LPS or vice versa.", epilog="Note that it is possible to specify a rotation by several distinct axes at the same time, but the behavior is not to rotate by one axis and then the other(s). Instead the behavior is the one of RotateWXYZ() function from vtkTransform class reference.")

    parser.add_argument("-i", "--input", required=True, help="Input track file (must be vtp or vtk).")
    parser.add_argument("-o", "--output", required=True, help="Desired name for output rotated track file.")
    parser.add_argument("-a", "--angle", type=int, required=False, default=180, help="Value of rotation angle.")
    parser.add_argument("-x", "--x_axis", action="store_true", help="Rotation around x_axis is done if -x is written.")
    parser.add_argument("-y", "--y_axis", action="store_true", help="Rotation around y_axis is done if -y is written.")
    parser.add_argument("-z", "--z_axis", action="store_true", help="Rotation around z_axis is done if -z is written.")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    rotation_angle = args.angle
    x_axis = 1 if args.x_axis else 0
    y_axis = 1 if args.y_axis else 0
    z_axis = 1 if args.z_axis else 0
    rotation(input_file, output_file, rotation_angle, x_axis, y_axis, z_axis)

    
