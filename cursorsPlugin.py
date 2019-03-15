import sublime
import sublime_plugin

# print text at cursor
# self.view.insert(edit, self.view.sel()[0].begin()
# , "CursorPlugin" + str(len(regions)))


class cursorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print('#############################################')
        print('####### Remove all except last cursor #######')
        regions = self.view.sel()
        lastRegion = regions[len(regions) - 1]
        lastRegion = sublime.Region(lastRegion.a, lastRegion.b)

        self.view.sel().clear()
        self.view.sel().add(lastRegion)
