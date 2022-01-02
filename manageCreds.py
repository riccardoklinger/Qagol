# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Qagol
                                 A QGIS plugin
 COnnect QGIS with AGOL
                              -------------------
        begin                : 2021-01-02
        copyright            : (C) 2021 by Riccardo Klinger
        email                : riccardo.klinger@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (
    QgsField,
    QgsFeature,
    QgsFeatureSink,
    QgsFeatureRequest,
    QgsProcessingParameterString,
    QgsSettings,
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterFeatureSink,
)


class manageAgolCreds(QgsProcessingAlgorithm):
    INPUT = "INPUT"
    INPUT2 = "INPUT2"
    INPUT3 = "INPUT3"

    def __init__(self):
        super().__init__()

    def name(self):
        return "exalgo"

    def tr(self, text):
        return QCoreApplication.translate("exalgo", text)

    def displayName(self):
        return self.tr("Example script")

    def group(self):
        return self.tr("Examples")

    def groupId(self):
        return "examples"

    def shortHelpString(self):
        return self.tr("Example script without logic")

    def helpUrl(self):
        return "https://qgis.org"

    def createInstance(self):
        return type(self)()

    def initAlgorithm(self, config=None):
        """Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.addParameter(
            QgsProcessingParameterString(self.INPUT, self.tr("API Key"))
        )
        self.addParameter(
            QgsProcessingParameterString(self.INPUT2, self.tr("AGOL user name"))
        )
        self.addParameter(
            QgsProcessingParameterString(self.INPUT3, self.tr("AGOL password"))
        )

    def processAlgorithm(self, parameters, context, feedback):
        """getting the api key"""
        s = QgsSettings()
        key = self.parameterAsString(parameters, self.INPUT, context)
        name = self.parameterAsString(parameters, self.INPUT2, context)
        pw = self.parameterAsString(parameters, self.INPUT3, context)

        s.setValue("Qagol/api_key", key)
        s.setValue("Qagol/username", name)
        s.setValue("Qagol/password", pw)

        feedback.pushInfo(
            """Success! Your API key was updated/saved and will be used for future placekey requests."""
        )
        return {}
