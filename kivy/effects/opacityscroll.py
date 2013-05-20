'''
Opacity scroll effect
=====================

Based on the :class:`~kivy.effects.damped.DampedScrollEffect`, this one will
also decrease the opacity of the target widget during the overscroll.

'''

__all__ = ('OpacityScrollEffect', )


from kivy.effects.dampedscroll import DampedScrollEffect


class OpacityScrollEffect(DampedScrollEffect):

    def on_overscroll(self, *args):
        if self.target_widget and self.target_widget.height != 0:
            alpha = 1.0 - abs(self.overscroll / float(self.target_widget.height))
            self.target_widget.opacity = min(1, alpha)
        self.trigger_velocity_update()

