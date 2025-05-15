from imswitch.imcommon.model import UIExport
from imswitch import IS_HEADLESS
if IS_HEADLESS:
    from imswitch.imcontrol.view.widgets.basewidgets import Widget


    class imswitch_lightsheet_widget(Widget):
        """Linked to the lightsheet Controller ."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class imswitch_lightsheetReactWidget(object):
    """"""
    print("react")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("init")

    @UIExport(
        path="/Users/bene/Downloads/imswitch-lightsheet/src/imswitch_lightsheet/ui/dist",                 # relative to **this** Python package
        name="Lightsheet",
        icon="ThreeDRotationIcon",
    )
    def getUIPath(self):
        return os.path.join(self._path, "lightsheetreactwidget")