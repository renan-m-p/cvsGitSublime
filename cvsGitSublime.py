import sublime, sublime_plugin, subprocess, json

class cvsGitSublime(sublime_plugin.TextCommand):
  
  def run(self, edit):  
    
    self.options = [];
    self.options.append("Status");
    self.options.append("Log");
    self.options.append("Pull");

    window = sublime.active_window()
    window.show_quick_panel(self.options, self.menu, sublime.MONOSPACE_FONT);

  def menu(self, escolha):

    if(escolha == 0):
      self.status()

    if(escolha == 1):
      self.log()

    if(escolha == 2):
      self.pull()

  def status(self):

    # output = subprocess.check_output("cd /var/www/dbportal_prj && cvsgit status -j", shell = True)
    # output = output.decode('ascii')
    output = self.cvsGit("status")
    
    # aDados = json.loads(output);
    # saida  = ''

    # for sTipoModificacao in aDados :
    #   aModificacoes = aDados[sTipoModificacao]

    #   if(len(aModificacoes) > 0):
    #     saida += sTipoModificacao + "\n"
            
    #   for oArquivo in aModificacoes :
    #     saida += oArquivo['sArquivo'] + "\n";
    

    self.abreTerminal(output);

  def log(self):

    # window = sublime.active_window()
    # teste = window.project_file_name();
    # print(teste)
    # self.abreTerminal(teste);

    sPath  = self.view.file_name();
    output = self.cvsGit("log " + sPath)
    self.abreTerminal(output)
    

  def pull(self):

    output = self.cvsGit("pull")
    self.abreTerminal(output)



  def cvsGit(self, sComando):
    output = subprocess.check_output("cd /var/www/dbportal_prj && cvsgit " + sComando, shell = True)
    output = output.decode('utf8')

    return output;

  def abreTerminal(self, texto):

    self.output_view = self.view.window().get_output_panel("textarea")
    window = sublime.active_window()
    window.run_command("show_panel", {"panel": "output.textarea"})
    self.output_view.set_read_only(False)
    self.output_view.run_command("append", {"characters": texto})








