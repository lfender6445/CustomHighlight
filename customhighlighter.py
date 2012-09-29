import sublime, sublime_plugin, re
import textwrap

class HighlightOptions:
    def __init__(self):
        self.color_highlight = ""
        self.words  = ""

s = sublime.load_settings("customhighlighter.sublime-settings")

def default_options():
    return HighlightOptions()

class HighlightCommand(sublime_plugin.TextCommand):

	def on_done():
		print("value")
	def run(self, edit):
		h = []
		settings = self.view.settings()
		opts = default_options()
		all_reg = []
		# settings
		opts.color_highlight = settings.get("color_highlight")
		opts.words  = s.get("words")


		for item in opts.words:
		    sel = self.view.find_all(item, sublime.LITERAL)
		    all_reg.append(sel)

		self.view.add_regions("WordHighlight", [item for sublist in all_reg for item in sublist], "circle", sublime.DRAW_EMPTY)