# Explore Startup SQLs

This uses a mixin (database/ALSBase) to attempt to override startup SQLs.

It is supposed to be electable, based on class variable in ALSBase.

It is not working (see database/log-)

1. If pre-flight is True, it fails

2. If pre-flight is False, it still issues many SQLs

To test, use a `venv` and press F5.