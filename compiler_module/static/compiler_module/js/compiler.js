$(document).ready(function() {
    var editor = CodeMirror.fromTextArea(document.getElementById("compilerarea"), {
        lineNumbers: true,
        mode: "python",
        matchBrackets: true,
        autoCloseBrackets: true,
        extraKeys: {
            "Ctrl-Space": "autocomplete"
        }
    });
});