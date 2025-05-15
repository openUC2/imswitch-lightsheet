import datetime
import imswitch
from imswitch.imcontrol.controller.basecontrollers import ImConWidgetController
from imswitch.imcommon.model.logging import initLogger
import numpy as np
from imswitch.imcommon.model import UIExport
import sys
import os 

_uiPath = os.path.join(os.path.dirname(__file__), "ui/dist")

class imswitch_lightsheet_controller(ImConWidgetController):
    """Linked to CameraPluginWidget."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__logger = initLogger(self)
        self.__logger.debug("Initializing imswitch arkitekt_next controller")
    
    
    @UIExport(
        path=_uiPath,                 # relative to **this** Python package
        name="Lightsheet",
        icon="ThreeDRotationIcon",
    )
    def getUIPath(self):
        return os.path.join(self._path, "lightsheetreactwidget")


# Copyright (C) 2020-2021 ImSwitch developers
# This file is part of ImSwitch.
#
# ImSwitch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ImSwitch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
