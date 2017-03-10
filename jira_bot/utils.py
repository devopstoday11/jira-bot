# -*- coding: utf-8 -*-
#
# Copyright (c) 2015-2017 Alex Turbov <i.zaufi@gmail.com>
#
# JIRA Bot is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# JIRA Bot is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


def form_value_using_dict(config, value, get_values_collection):
    ''' TODO Better name?
    '''
    assert isinstance(config, dict) and 0 < len(config)

    if config[value].isdigit():
        return {'id' : config[value]}

    else:
        values = [v.name for v in get_values_collection()]

        if config[value] in values:
            return {'name' : config[value]}

        raise RuntimeError('Given {} not in a list of allowed values: {}'.format(value, ', '.join(values)))
