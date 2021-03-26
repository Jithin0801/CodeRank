$(document).ready(function() {
    var editor = CodeMirror.fromTextArea(document.getElementById("compilerarea"), {
        lineNumbers: true,
        mode: "python",
        matchBrackets: true,
        lineWrapping: true,
        theme: "dracula",
        autoCloseBrackets: true,
        extraKeys: {
            "Ctrl-Space": "autocomplete"
        }
    });

    editor.setValue("print(\'CodeRank\')")
});