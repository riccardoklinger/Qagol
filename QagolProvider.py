# -*- coding: utf-8 -*-

"""
/***************************************************************************
 placekey
                                 A QGIS plugin
 Processing plugin for placekey
                              -------------------
        begin                : 2020-11-12
        copyright            : (C) 2020 by Riccardo Klinger
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

from qgis.core import QgsProcessingProvider
from .manageCreds import manageAgolCreds

__author__ = "Riccardo Klinger"
__date__ = "2022-01-02"
__copyright__ = "(C) 2021 by Riccardo Klinger"

__revision__ = "$Format:%H$"


class qagolProvider(QgsProcessingProvider):
    def __init__(self):
        QgsProcessingProvider.__init__(self)

        self.activate = False

    def unload(self):
        """Setting should be removed here, so they do not appear anymore
        when the plugin is unloaded.
        """
        QgsProcessingProvider.unload(self)

    def id(self):
        """This is the name that will appear on the toolbox group.

        It is also used to create the command line name of all the
        algorithms from this provider.
        """
        return "Qagol"

    def name(self):
        """This is the provired full name."""
        return "Qagol"

    def icon(self):
        """We return the default icon."""
        return QgsProcessingProvider.icon(self)

    def load(self):
        self.refreshAlgorithms()
        return True

    def loadAlgorithms(self):
        """Here we fill the list of algorithms in self.algs.

        This method is called whenever the list of algorithms should
        be updated. If the list of algorithms can change (for instance,
        if it contains algorithms from user-defined scripts and a new
        script might have been added), you should create the list again
        here.

        In this case, since the list is always the same, we assign from
        the pre-made list. This assignment has to be done in this method
        even if the list does not change, since the self.algs list is
        cleared before calling this method.
        """
        self.alglist = [manageAgolCreds()]
        for alg in self.alglist:
            self.addAlgorithm(alg)
