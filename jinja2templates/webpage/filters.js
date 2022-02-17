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
    let input_search_txt = document.getElementById('search_txt_filter').elements[0].value;

    for (let card of cards) {
        var card_id = card.id.split("_").pop();
        var card_data = data[card_id];
        var hide = false;
        for (let key in dict) {
            if (!dict[key].includes(card_data[key].toString())) {
                hide = true;
            }
        }

        hide = hide || check_card_for_txt_search(card_data, input_search_txt)

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

function check_card_for_txt_search(card_data,input_search_txt) {
    var hide = false;
    if (
        {% for column in columns_to_be_searched %}
            !card_data['{{column}}'].toLowerCase().includes(input_search_txt.toLowerCase()) &&
        {% endfor %} true
        )
    {
        hide = true;
    }
    return hide;
}

function on_filters_change() {
    var dict = get_dict_of_all_filters();
    hide_cards_not_in_active_filters(dict);
}


function onclick_reset_filter(filter_id) {
    document.getElementById(filter_id).reset();
    on_filters_change();
}   
