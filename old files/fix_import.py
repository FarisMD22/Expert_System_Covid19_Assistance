"""
Compatibility Patch for Experta with Python 3.10+

This module patches the collections module to restore compatibility
with the experta library when using Python 3.10 or later.

Usage:
    Place this file in your project root and import it BEFORE importing experta:

    import fix_imports  # Import this FIRST
    from experta import Fact, KnowledgeEngine  # Now this will work

Issue:
    Python 3.10+ moved abstract base classes from collections to collections.abc
    The experta library (and its dependency frozendict) still reference the old location

Solution:
    This script adds the abstract base classes back to the collections module
    as aliases to their new locations in collections.abc

Author: TES6313 CIDAS Project
Date: 2025
"""

import sys
import collections
import collections.abc

# List of abstract base classes that were moved
ABC_CLASSES = [
    'Callable', 'Iterable', 'Iterator', 'Reversible',
    'Container', 'Collection', 'Sized',
    'Hashable', 'Awaitable', 'Coroutine', 'AsyncIterable', 'AsyncIterator',
    'Mapping', 'MutableMapping', 'MappingView', 'KeysView', 'ItemsView', 'ValuesView',
    'Sequence', 'MutableSequence',
    'Set', 'MutableSet',
    'ByteString'
]

# Apply patches
patched = []
for class_name in ABC_CLASSES:
    if hasattr(collections.abc, class_name) and not hasattr(collections, class_name):
        setattr(collections, class_name, getattr(collections.abc, class_name))
        patched.append(class_name)

# Report results
if patched:
    print(f"✓ Compatibility patch applied: {len(patched)} classes restored to collections module")
    print(f"  Python version: {sys.version}")
    print(f"  Experta should now work correctly with Python {sys.version_info.major}.{sys.version_info.minor}")
else:
    print("✓ No patching needed (Python 3.9 or earlier, or already patched)")