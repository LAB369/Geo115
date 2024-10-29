# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Feature Merge Toolbox"
        self.alias = "featuremerge"
        # List of tool classes associated with this toolbox
        self.tools = [MergeFeatures]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Merge Features"
        self.description = "Merges two or more feature classes or feature layers."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define the tool parameters."""
        param0 = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input",
            multiValue=True)
        param1 = arcpy.Parameter(
            displayName="Output Feature Class",
            name="out_feature_class",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output")
        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal validation is performed.  This method is called whenever a parameter has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_features = parameters[0].valueAsText
        output_feature_class = parameters[1].valueAsText
        # Split the input features string into a list
        input_features_list = input_features.split(";")
        # Perform the merge
        arcpy.Merge_management(input_features_list, output_feature_class)
        messages.addMessage("Merge completed successfully.")
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and added to the display."""
        return
