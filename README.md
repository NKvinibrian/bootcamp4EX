<h2>Criar uma venv:</h2>
<p><code class="samp docutils literal notranslate"><span class="pre">python -m venv venv</span></code></p>


<h2>Iniciar a venv:</h2>
<table class="docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 16%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Sistemas</p></th>
<th class="head"><p>Terminais / Shell</p></th>
<th class="head"><p>Comando para ativar o virtual environment(venv)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="4"><p>POSIX / Linux</p></td>
<td><p>bash/zsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>fish</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate.fish</span></code></p></td>
</tr>
<tr class="row-even"><td><p>csh/tcsh</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <span class="pre">source</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/activate.csh</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>PowerShell</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">$</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">/bin/Activate.ps1</span></code></p></td>
</tr>
<tr class="row-even"><td rowspan="2"><p>Windows</p></td>
<td><p>cmd.exe</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">C:\&gt;</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">\Scripts\activate.bat</span></code></p></td>
</tr>
<tr class="row-odd"><td><p>PowerShell</p></td>
<td><p><code class="samp docutils literal notranslate"><span class="pre">PS</span> <span class="pre">C:\&gt;</span> <em><span class="pre">&lt;venv&gt;</span></em><span class="pre">\Scripts\Activate.ps1</span></code></p></td>
</tr>
</tbody>
</table>

<h2>Instalar as bibliotecas na venv:</h2>
<p><code class="samp docutils literal notranslate"><span class="pre">pip install -r requirements.txt</span></code></p>

<h2>Comandos migrates:</h2>
<p><code class="samp docutils literal notranslate"><span class="pre">python manage.py makemigrations</span></code></p>
<p><code class="samp docutils literal notranslate"><span class="pre">python manage.py migrate</span></code></p>

<h2>Rodar o servidor:</h2>
<p><code class="samp docutils literal notranslate"><span class="pre">python manage.py runserver</span></code></p>
