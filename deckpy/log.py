'''
	DeckPy is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	DeckPy is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with DeckPy: see gpl3.txt at the top of the program directory.
	If not, see <http://www.gnu.org/licenses/>.
'''
import logging
import sys

format = "[%(asctime)s] (%(name)s) %(message)s"
def stderr_logger(name):
	dp_log = logging.getLogger(name)

	handler = logging.StreamHandler(stream = sys.stderr)
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(logging.Formatter(format))

	dp_log.addHandler(handler)

	return dp_log


	