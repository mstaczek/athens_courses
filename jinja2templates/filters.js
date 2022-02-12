var data = {{ js_dict | safe }};
var cards = document.querySelectorAll('[id^="course_card_"]');
var forms = document.querySelectorAll('[id^="filter_"]');

function get_currently_checked(form_id) {
    var form = document.getElementById(form_id);
    var checked = [];
    var unchecked = [];
    for (var i = 0; i < form.elements.length; i++) {
        if (form.elements[i].checked) {
            checked.push(form.elements[i].value);
        }
        else {
            unchecked.push(form.elements[i].value);
        }
    }
    return { 'checked': checked, 'unchecked': unchecked };
}

function get_dict_of_all_filters() {
    var dict = {};
    for (let form of forms) {
        var column_name = form.id.split("_").slice(1);
        var checked = get_currently_checked(form.id);
        if (checked['checked'].length > 0) {
            dict[column_name] = checked['checked'];
        }
    }
    return dict;
}

function hide_cards_not_in_active_filters(dict) {
    for (let card of cards) {
        var card_id = card.id.split("_").pop();
        var card_data = data[card_id];
        var hide = false;
        for (let key in dict) {
            if (!dict[key].includes(card_data[key].toString())) {
                hide = true;
            }
        }
        if (hide) {
            card.classList.add("hidden_card"); 
            card.classList.remove("not_hidden_card");
        }
        else {
            card.classList.add("not_hidden_card");
            card.classList.remove("hidden_card"); 
        }
    }
}

function on_filters_change() {
    var dict = get_dict_of_all_filters();
    hide_cards_not_in_active_filters(dict);
}

function onclick_reset_filter(filter_id){
    document.getElementById(filter_id).reset();
    on_filters_change();
}   
