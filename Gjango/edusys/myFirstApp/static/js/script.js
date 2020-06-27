function DayClick(dayNum, obj) {
    if ($(obj).hasClass('selected') && ($('#Schedule table tbody tr td.d' + dayNum + ' div.selected').length)) {
        $('#Schedule table tbody tr td.d' + dayNum + ' div').removeClass('selected');
        $(obj).removeClass('selected');
    }
    else {
        $('#Schedule table tbody tr td.d' + dayNum + ' div').addClass('selected');
        $(obj).addClass('selected');
    };
}
$(document).ready(function() {
    $('#Schedule table tbody tr .d0').hover(
        function() { $('#Schedule table thead tr td.d0').addClass('hovered') },
        function() { $('#Schedule table thead tr td.d0').removeClass('hovered') });
    $('#Schedule table thead tr .d0').hover(
        function() { $('#Schedule table td.d0').addClass('hovered') },
        function() { $('#Schedule table td.d0').removeClass('hovered') })
            .click(function() { DayClick('0', this) });

    $('#Schedule table tbody tr .d1').hover(
        function() { $('#Schedule table thead tr td.d1').addClass('hovered') },
        function() { $('#Schedule table thead tr td.d1').removeClass('hovered') });
    $('#Schedule table thead tr .d1').hover(
        function() { $('#Schedule table td.d1').addClass('hovered') },
        function() { $('#Schedule table td.d1').removeClass('hovered') })
            .click(function() { DayClick('1', this) });

    $('#Schedule table tbody tr .d2').hover(
        function() { $('#Schedule table thead tr td.d2').addClass('hovered') },
        function() { $('#Schedule table thead tr td.d2').removeClass('hovered') });
    $('#Schedule table thead tr .d2').hover(
        function() { $('#Schedule table td.d2').addClass('hovered') },
        function() { $('#Schedule table td.d2').removeClass('hovered') })
            .click(function() { DayClick('2', this) });

    $('#Schedule table tbody tr .d3').hover(
        function() { $('#Schedule table thead tr td.d3').addClass('hovered') },
        function() { $('#Schedule table thead tr td.d3').removeClass('hovered') });
    $('#Schedule table thead tr .d3').hover(
        function() { $('#Schedule table td.d3').addClass('hovered') },
        function() { $('#Schedule table td.d3').removeClass('hovered') })
            .click(function() { DayClick('3', this) });

    $('#Schedule table tbody tr .d4').hover(
        function() { $('#Schedule table thead tr td.d4').addClass('hovered') },
        function() { $('#Schedule table thead tr td.d4').removeClass('hovered') });
    $('#Schedule table thead tr .d4').hover(
        function() { $('#Schedule table td.d4').addClass('hovered') },
        function() { $('#Schedule table td.d4').removeClass('hovered') })
            .click(function() { DayClick('4', this) });

    $('#Schedule table tbody tr .d5').hover(
        function() { $('#Schedule table thead tr td.d5').addClass('hovered') },
        function() { $('#Schedule table thead tr td.d5').removeClass('hovered') });
    $('#Schedule table thead tr .d5').hover(
        function() { $('#Schedule table td.d5').addClass('hovered') },
        function() { $('#Schedule table td.d5').removeClass('hovered') })
            .click(function() { DayClick('5', this) });

    $('#Schedule table tbody tr .d6').hover(
        function() { $('#Schedule table thead tr td.d6').addClass('hovered') },
        function() { $('#Schedule table thead tr td.d6').removeClass('hovered') });
    $('#Schedule table thead tr .d6').hover(
        function() { $('#Schedule table td.d6').addClass('hovered') },
        function() { $('#Schedule table td.d6').removeClass('hovered') })
            .click(function() { DayClick('6', this) });

    $('#Schedule table tr').hover(
        function() { $(this).addClass('hovered') },
        function() { $(this).removeClass('hovered') });
    $('#Schedule table tbody tr td div').click(
        function() { $(this).toggleClass('selected') });
});

function SubmitSchedule() {
    var XMLSchedule = "<week>";

    for (var d = 0; d < 7; d++) {
        XMLSchedule += '<d id="' + d + '">'
        for (var h = 7; h < 21; h++) {

            if ($('#Schedule table tbody tr.h' + h + ' td.d' + d + ' div').hasClass('selected')) {
                XMLSchedule += '<h v="' + h + '">1</h>';
            }
            else {
                XMLSchedule += '<h v="' + h + '">0</h>';
            };
        }
        XMLSchedule += '</d>';
    }
    XMLSchedule += "</week>";
    $('#output').text(XMLSchedule);
}