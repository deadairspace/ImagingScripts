#include <vtkVersion.h>
#include <vtkNew.h>
#include <vtkSmartPointer.h>
#include <vtkImageData.h>
#include <vtkStringArray.h>
#include <vtkTIFFReader.h>
#include <vtkXMLImageDataWriter.h>
#include <iostream>
#include <sstream>
#include <vtkImageResample.h>

#include "boost/format.hpp"

int main(int, char *[])
{
  std::string inputFilename = "/Volumes/Macintosh HD 2/For_Stephen/B100_2.6/Recon_FFT_";
  std::string extension = ".tif";

  std::size_t N = 1927;
  
  vtkNew<vtkStringArray> filenames;
  vtkNew<vtkTIFFReader> reader;

  for(std::size_t i = 115; i< N; ++i)
  {
    std::stringstream ss;
    ss << inputFilename << boost::format("%0004d") % i << extension;
    filenames->InsertNextValue(ss.str());
    std::cout << ss.str() << std::endl;
    //reader->SetFileName(ss.str().c_str());
    //reader->Update();
    //vtkImageData* readDataset(reader->GetOutput());
    //int* dims = readDataset->GetDimensions();
    //std::cout << "Dims: " << " x: " << dims[0] << " y: " << dims[1] << " z: " << dims[2] << std::endl;
    
  }
  
  reader->SetFileNames(filenames.GetPointer());
  reader->Update();
  reader->Print(std::cout);
  
  vtkImageData* readDataset(reader->GetOutput());
  int* dims = readDataset->GetDimensions();
  std::cout << "Dims: " << " x: " << dims[0] << " y: " << dims[1] << " z: " << dims[2] << std::endl;
  
  double reductionFactor = 0.25;
  vtkNew<vtkImageResample> resample;
  resample->SetInputConnection(reader->GetOutputPort());
  resample->SetAxisMagnificationFactor(0, reductionFactor);
  resample->SetAxisMagnificationFactor(1, reductionFactor);
  resample->SetAxisMagnificationFactor(2, reductionFactor);
  resample->SetDimensionality(3);
  resample->Update();
  resample->UpdateWholeExtent();
  
  vtkImageData* IMreadDataset = resample->GetOutput();
  int* newdims = IMreadDataset->GetDimensions();
  double* spacing = IMreadDataset->GetSpacing();
  
  std::cout << "Dims: " << " x: " << newdims[0] << " y: " << newdims[1] << " z: " << newdims[2] << std::endl;
  std::cout << "x: " << spacing[0] << " y: " << spacing[1] << " z: " << spacing[2] << std::endl;
  
  vtkNew<vtkXMLImageDataWriter> writer;
  writer->SetFileName("test1p0.vti");
  writer->SetInputData(IMreadDataset);
  writer->SetDataModeToBinary();
  writer->SetCompressorTypeToNone();
  //writer->SetHeaderTypeToUInt64();
  writer->Write();
  
  return EXIT_SUCCESS;
}
