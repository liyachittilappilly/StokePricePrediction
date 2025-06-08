<html>
<head>
<title>app.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #6aab73;}
.s4 { color: #7a7e85;}
.s5 { color: #2aacb8;}
.ln { color: #4b5059; font-weight: normal; font-style: normal; }
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
app.py</font>
</center></td></tr></table>
<pre><a name="l1"><span class="ln">1    </span></a><span class="s0">from </span><span class="s1">flask </span><span class="s0">import </span><span class="s1">Flask</span><span class="s2">, </span><span class="s1">render_template</span><span class="s2">, </span><span class="s1">request</span>
<a name="l2"><span class="ln">2    </span></a><span class="s0">import </span><span class="s1">pickle</span>
<a name="l3"><span class="ln">3    </span></a><span class="s0">import </span><span class="s1">numpy </span><span class="s0">as </span><span class="s1">np</span>
<a name="l4"><span class="ln">4    </span></a>
<a name="l5"><span class="ln">5    </span></a><span class="s1">app </span><span class="s2">= </span><span class="s1">Flask</span><span class="s2">(</span><span class="s1">__name__</span><span class="s2">)</span>
<a name="l6"><span class="ln">6    </span></a><span class="s0">import </span><span class="s1">joblib</span>
<a name="l7"><span class="ln">7    </span></a><span class="s1">model </span><span class="s2">= </span><span class="s1">joblib</span><span class="s2">.</span><span class="s1">load</span><span class="s2">(</span><span class="s3">'model.pkl'</span><span class="s2">)</span>
<a name="l8"><span class="ln">8    </span></a>
<a name="l9"><span class="ln">9    </span></a>
<a name="l10"><span class="ln">10   </span></a>
<a name="l11"><span class="ln">11   </span></a><span class="s2">@</span><span class="s1">app</span><span class="s2">.</span><span class="s1">route</span><span class="s2">(</span><span class="s3">'/'</span><span class="s2">)</span>
<a name="l12"><span class="ln">12   </span></a><span class="s0">def </span><span class="s1">home</span><span class="s2">():</span>
<a name="l13"><span class="ln">13   </span></a>    <span class="s0">return </span><span class="s1">render_template</span><span class="s2">(</span><span class="s3">'index.html'</span><span class="s2">)</span>
<a name="l14"><span class="ln">14   </span></a>
<a name="l15"><span class="ln">15   </span></a>
<a name="l16"><span class="ln">16   </span></a><span class="s2">@</span><span class="s1">app</span><span class="s2">.</span><span class="s1">route</span><span class="s2">(</span><span class="s3">'/predict/'</span><span class="s2">, </span><span class="s1">methods</span><span class="s2">=[</span><span class="s3">'POST'</span><span class="s2">])</span>
<a name="l17"><span class="ln">17   </span></a><span class="s0">def </span><span class="s1">predict</span><span class="s2">():</span>
<a name="l18"><span class="ln">18   </span></a>    <span class="s4"># Get form data</span>
<a name="l19"><span class="ln">19   </span></a>    <span class="s1">open_price </span><span class="s2">= </span><span class="s1">float</span><span class="s2">(</span><span class="s1">request</span><span class="s2">.</span><span class="s1">form</span><span class="s2">[</span><span class="s3">'Open'</span><span class="s2">])</span>
<a name="l20"><span class="ln">20   </span></a>    <span class="s1">high_price </span><span class="s2">= </span><span class="s1">float</span><span class="s2">(</span><span class="s1">request</span><span class="s2">.</span><span class="s1">form</span><span class="s2">[</span><span class="s3">'High'</span><span class="s2">])</span>
<a name="l21"><span class="ln">21   </span></a>    <span class="s1">low_price </span><span class="s2">= </span><span class="s1">float</span><span class="s2">(</span><span class="s1">request</span><span class="s2">.</span><span class="s1">form</span><span class="s2">[</span><span class="s3">'Low'</span><span class="s2">])</span>
<a name="l22"><span class="ln">22   </span></a>    <span class="s1">volume </span><span class="s2">= </span><span class="s1">float</span><span class="s2">(</span><span class="s1">request</span><span class="s2">.</span><span class="s1">form</span><span class="s2">[</span><span class="s3">'Volume'</span><span class="s2">])</span>
<a name="l23"><span class="ln">23   </span></a>
<a name="l24"><span class="ln">24   </span></a>    <span class="s4"># Format data for model</span>
<a name="l25"><span class="ln">25   </span></a>    <span class="s1">features </span><span class="s2">= </span><span class="s1">np</span><span class="s2">.</span><span class="s1">array</span><span class="s2">([[</span><span class="s1">open_price</span><span class="s2">, </span><span class="s1">high_price</span><span class="s2">, </span><span class="s1">low_price</span><span class="s2">, </span><span class="s1">volume</span><span class="s2">]])</span>
<a name="l26"><span class="ln">26   </span></a>
<a name="l27"><span class="ln">27   </span></a>    <span class="s4"># Predict</span>
<a name="l28"><span class="ln">28   </span></a>    <span class="s1">prediction </span><span class="s2">= </span><span class="s1">model</span><span class="s2">.</span><span class="s1">predict</span><span class="s2">(</span><span class="s1">features</span><span class="s2">)</span>
<a name="l29"><span class="ln">29   </span></a>
<a name="l30"><span class="ln">30   </span></a>    <span class="s4"># Return the result in a new page</span>
<a name="l31"><span class="ln">31   </span></a>    <span class="s0">return </span><span class="s1">render_template</span><span class="s2">(</span><span class="s3">'prediction.html'</span><span class="s2">, </span><span class="s1">prediction</span><span class="s2">=</span><span class="s1">round</span><span class="s2">(</span><span class="s1">prediction</span><span class="s2">[</span><span class="s5">0</span><span class="s2">], </span><span class="s5">2</span><span class="s2">))</span>
<a name="l32"><span class="ln">32   </span></a>
<a name="l33"><span class="ln">33   </span></a>
<a name="l34"><span class="ln">34   </span></a><span class="s0">if </span><span class="s1">__name__ </span><span class="s2">== </span><span class="s3">&quot;__main__&quot;</span><span class="s2">:</span>
<a name="l35"><span class="ln">35   </span></a>    <span class="s1">app</span><span class="s2">.</span><span class="s1">run</span><span class="s2">(</span><span class="s1">debug</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>
<a name="l36"><span class="ln">36   </span></a></pre>
</body>
</html>
