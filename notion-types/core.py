# Base Types
# ----------------------------------------------------------------------------

from typing import NewType, Protocol, Union, Literal
from dataclasses import dataclass

# UUID
ID: str

# Unique identifier for collection properties representing the columns in a
# traditional relational database.
#
# Either a 4-character hash like `o;Os` or `title` as a special, reserved
# property ID for collection title properties.
#
# You can think of `title` properties as primary indexes that are guaranteed
# to exist as in a traditional database.


PropertyID = NewType("PropertyID", str)

# Block colors supported by Notion
Color = Literal[
   'gray',
   'brown',
   'orange',
   'yellow',
   'teal',
   'blue',
   'purple',
   'pink',
   'red',
   'gray_background',
   'brown_background',
   'orange_background',
   'yellow_background',
   'teal_background',
   'blue_background',
   'purple_background',
   'pink_background',
   'red_background',
]


# Types of structured data supported by Notion collections
PropertyType = Literal[
    'title',
    'text',
    'number',
    'select',
    'multi_select',
    'date',
    'person',
    'file',
    'checkbox',
    'url',
    'email',
    'phone_number',
    'formula',
    'relation',
    'created_time',
    'created_by',
    'last_edited_time',
    'last_edited_by',
]


# Types of number formatting supported by Notion
NumberFormat = Literal[
    'number_with_commas',
    'percent',
    'dollar',
    'euro',
    'pound',
    'yen',
    'rupee',
    'won',
    'yuan',
]

Role = Literal['editor' , 'reader' , 'none' , 'read_and_write']


@dataclass
class FormattedDate:
    _type: str
    start_date: str
    start_time: str
    end_date: str
    end_time: str
    date_format: str
    time_zone: str

BoldFormat = Literal['b']
ItalicFormat = ['i']
StrikeFormat = ['s']
CodeFormat = ['c']
UnderlineFormat = ['_']
LinkFormat = ['a', str]
ExternalObjectInstanceFormat = ['eoi', str]
ColorFormat = ['h', Color]
UserFormat = ['u', str]
PageFormat = ['p', str]
InlineEquationFormat = ['e', str]
DiscussionFormat = ['m', str]
ExternalLinkFormat = ['‣', [str, str]]
DateFormat = ['d', FormattedDate]

# Subdecoration = Literal[
#     BoldFormat,
#     ItalicFormat,
#     StrikeFormat,
#     CodeFormat,
#     UnderlineFormat,
#     LinkFormat,
#     ExternalLinkFormat,
#     ColorFormat,
#     UserFormat,
#     PageFormat,
#     InlineEquationFormat,
#     DiscussionFormat,
#     ExternalObjectInstanceFormat,
#     DateFormat,
# ]