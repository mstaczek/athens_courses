function on_sort_change() {
    let column = get_currently_checked("sort_dropdown_column")['unchecked'][0];
    let ascdesc = get_currently_checked("sort_dropdown_asc_desc")['unchecked'][0];

    var ids_order = [...Array(cards.length).keys()]
    ids_order.sort(get_sorting_function(column));
    if (parseInt(ascdesc) == 1) {
        ids_order.reverse();
    }
    let parent_accordion = document.getElementById("accordion");
    for (var i = 0; i < cards.length; i++) {
        parent_accordion.appendChild(cards[ids_order[i]]);
    }
}

function get_sorting_function(column) {    
    return function (a, b) {
        // if (a is less than b by some ordering criterion) 
        if (data[a][column] < data[b][column]) {
            return -1;
        }
        // if (a is greater than b by the ordering criterion) 
        if (data[a][column] > data[b][column]) {
            return 1;
        }
        // if (a equals b)
        return 0;
    }
}

on_sort_change();