import sublime, sublime_plugin, re
import textwrap

class HighlightOptions:
    def __init__(self):
        self.color_highlight = ""
        self.words_included  = ""

s = sublime.load_settings("customhighlight.sublime-settings")
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
		# sel = self.view.sel()[0]
		# print(sel)
		# # settings
		opts.color_highlight = s.get("color_highlight")
		opts.words_included  = s.get("words_included")
		print("words")
		print(opts.words_included)

		for item in opts.words_included:
			print("trying")
			print(item)
			sel = self.view.find_all(item, sublime.LITERAL)
			all_reg.append(sel)

		self.view.add_regions("WordHighlight", [item for sublist in all_reg for item in sublist], "circle", sublime.DRAW_EMPTY)


		for reg in all_reg:
			print(reg)
			# self.view.add_regions("WordHighlight", reg, "circle", sublime.DRAW_EMPTY)


			# self.view.fold(reg)
			# sel(0)
			# self.view.window().show_quick_panel(opts.words_included, self.on_done, sublime.MONOSPACE_FONT)