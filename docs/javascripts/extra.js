var replaceWith = " - Foxford Docs";

setInterval(() => {
    function truncate(str, n){
        return (str.length > n) ? str.slice(0, n-1).trim() + '...' : str;
    };
    
    if (document.title.endsWith(" - Foxford") && document.title != "Sniff-sniff... 404 smell...") {
        document.title = truncate(document.title.slice(0, -10), 8) + " - Foxford Docs";
    }
}, 1);