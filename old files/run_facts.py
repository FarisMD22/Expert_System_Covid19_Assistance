"""
Wrapper script to run facts.py with Python 3.10+ compatibility
This patches collections BEFORE importing experta
"""

# PATCH FIRST - before ANY imports
import collections
import collections.abc
for attr in ['Mapping', 'MutableMapping', 'Iterable', 'Iterator', 'Callable',
             'Set', 'MutableSet', 'Sequence', 'MutableSequence', 'Hashable',
             'Sized', 'Container', 'Collection', 'Reversible', 'Generator',
             'ByteString', 'Awaitable', 'Coroutine', 'AsyncIterable', 'AsyncIterator']:
    if hasattr(collections.abc, attr) and not hasattr(collections, attr):
        setattr(collections, attr, getattr(collections.abc, attr))

print("✓ Python 3.12 compatibility patch applied")

# Now run facts.py
exec(open('../facts.py').read())