// Go to https://register.athensnetwork.eu/courses
// then open js console in this page and paste the code below
// Wait until you see the results (list of links),
// then copy them to some txt, for example to 'links_2022_1.txt',
// then save and links are ready ;)

// Note - you must log out if registration is currently open!

// If page loads slowly and not all course pages were opened
// change the delay (2s is should be sufficient though)

(async function() {
    const delay = ms => new Promise(res => setTimeout(res, ms));
    let out = ""
    let n = document.querySelectorAll("accordion-group button").length
    for(i=0;i<document.querySelectorAll("accordion-group button").length;i++) {
        document.querySelectorAll("accordion-group button")[i].click()
        await delay(1000);
        out += window.location.href + "\n"
        history.back()
        await delay(1000)
        while(document.querySelectorAll("accordion-group button").length != n) {
            await delay(1000)
        }
    }
    console.log(out)
    console.log("Length: " + out.length)
    return out
})()