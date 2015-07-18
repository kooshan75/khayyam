# -*- coding: utf-8 -*-
__author__ = 'vahid'

MINYEAR = 1
MAXYEAR = 3178

PERSIAN_WEEKDAY_NAMES = {
            0: u'شنبه',
            1: u'یکشنبه',
            2: u'دوشنبه',
            3: u'سه شنبه',
            4: u'چهارشنبه',
            5: u'پنجشنبه',
            6: u'جمعه'
}
PERSIAN_WEEKDAY_NAMES_REGEX = u'(%s)' % '|'.join(PERSIAN_WEEKDAY_NAMES.values())

PERSIAN_WEEKDAY_ABBRS = {
            0: u'ش',
            1: u'ی',
            2: u'د',
            3: u'س',
            4: u'چ',
            5: u'پ',
            6: u'ج'
}
PERSIAN_WEEKDAY_ABBRS_REGEX = u'[%s]' % ''.join(PERSIAN_WEEKDAY_ABBRS.values())

PERSIAN_MONTH_NAMES = {
            1:  u'فروردین',
            2:  u'اردیبهشت',
            3:  u'خرداد',
            4:  u'تیر',
            5:  u'مرداد',
            6:  u'شهریور',
            7:  u'مهر',
            8:  u'آبان',
            9:  u'آذر',
            10: u'دی',
            11: u'بهمن',
            12: u'اسفند'}
PERSIAN_MONTH_NAMES_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_NAMES.values())

PERSIAN_MONTH_ABBRS = {
            1:  u'فر',
            2:  u'ار',
            3:  u'خر',
            4:  u'تی',
            5:  u'مر',
            6:  u'شه',
            7:  u'مه',
            8:  u'آب',
            9:  u'آذ',
            10: u'دی',
            11: u'به',
            12: u'اس'}
PERSIAN_MONTH_ABBRS_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_ABBRS.values())


PERSIAN_WEEKDAY_NAMES_ASCII = {
            0: 'Shanbeh',
            1: 'Yekshanbeh',
            2: 'Doshanbeh',
            3: 'Seshanbeh',
            4: 'Chaharshanbeh',
            5: 'Panjshanbeh',
            6: 'Jomeh',
}
PERSIAN_WEEKDAY_NAMES_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_WEEKDAY_NAMES_ASCII.values())


PERSIAN_WEEKDAY_ABBRS_ASCII= {
            0: 'Sh',
            1: 'Y',
            2: 'D',
            3: 'Se',
            4: 'Ch',
            5: 'P',
            6: 'J'
}
PERSIAN_WEEKDAY_ABBRS_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_WEEKDAY_ABBRS_ASCII.values())


PERSIAN_MONTH_NAMES_ASCII = {
            1:  'Farvardin',
            2:  'Ordibehesht',
            3:  'Khordad',
            4:  'Tir',
            5:  'Mordad',
            6:  'Shahrivar',
            7:  'Mehr',
            8:  'Aban',
            9:  'Azar',
            10: 'Dey',
            11: 'Bahman',
            12: 'Esfand'
}
PERSIAN_MONTH_NAMES_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_NAMES_ASCII.values())


PERSIAN_MONTH_ABBRS_ASCII= {
            1:  'F',
            2:  'O',
            3:  'Kh',
            4:  'T',
            5:  'Mo',
            6:  'Sh',
            7:  'M',
            8:  'Ab',
            9:  'Az',
            10: 'D',
            11: 'B',
            12: 'E'}
PERSIAN_MONTH_ABBRS_ASCII_REGEX = u'(%s)' % '|'.join(PERSIAN_MONTH_ABBRS_ASCII.values())


SATURDAY = 0
SUNDAY = 1
MONDAY = 2
TUESDAY = 3
WEDNESDAY = 4
THURSDAY = 5
FRIDAY = 6


YEAR_REGEX = '\d{1,4}'
SHORT_YEAR_REGEX = '\d{2}'
MONTH_REGEX = '([0]?[1-9]|1[0-2])'
DAY_REGEX = '([0]?[1-9]|[12]\d|3[01])'
DAY_OF_YEAR_REGEX = '\d{1,3}' # TODO: Precisest pattern
WEEK_OF_YEAR_REGEX = '\d{1,2}' # TODO: Precisest pattern
WEEKDAY_REGEX = '[0-6]'


HOUR12_REGEX = '\d{1,2}' # TODO: Precisest pattern
HOUR24_REGEX = '\d{1,2}' # TODO: Precisest pattern
MINUTE_REGEX = '\d{1,2}' # TODO: Precisest pattern
SECOND_REGEX = '\d{1,2}' # TODO: Precisest pattern
MICROSECOND_REGEX = '\d{1,6}'

LOCAL_DATE_FORMAT_REGEX = '%s %s %s %s' % (
    PERSIAN_WEEKDAY_NAMES_REGEX,
    DAY_REGEX,
    PERSIAN_MONTH_NAMES_REGEX,
    YEAR_REGEX
)

FORMAT_DIRECTIVE_REGEX = '%[a-zA-Z%]'

AM_PM = {0: u'ق.ظ',
         1: u'ب.ظ'}
AM_PM_REGEX = u'(%s)' % u'|'.join(AM_PM.values())

AM_PM_ASCII = {0: 'AM',
               1: 'PM'}
AM_PM_ASCII_REGEX = '([aA][mM]|[pP][mM])'