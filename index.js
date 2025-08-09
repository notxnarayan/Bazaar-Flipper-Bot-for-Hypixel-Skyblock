const Toolkit = Java.type("java.awt.Toolkit");
const StringSelection = Java.type("java.awt.datatransfer.StringSelection");

function copyToClipboard(text) {
    const selection = new StringSelection(text);
    const clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
    clipboard.setContents(selection, null);
    ChatLib.chat("&aCopied trigger to clipboard!");
}

// Trigger from chat
register("chat", (message) => {
    if (message.toLowerCase().includes("your buy order for")) {
        copyToClipboard("BUY_TRIGGER"+message);
    }
    if (message.toLowerCase().includes("your sell offer for")) {
        copyToClipboard("SELL_TRIGGER"+message);
    }
}).setCriteria("${message}");
