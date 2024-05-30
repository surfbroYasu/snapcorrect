$.ajaxSetup({
  beforeSend: function beforeSend(xhr, settings) {
    function getCookie(name) {
      let cookieValue = null;

      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');

        for (let i = 0; i < cookies.length; i += 1) {
          const cookie = jQuery.trim(cookies[i]);

          if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }

      return cookieValue;
    }

    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
      xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    }
  },
});


$(document).ready(function () {
  $("#dropdown-menu").on("click", function (e) {
    $("#menu").fadeToggle();
  })

  $(".js-comment-button").on("click", function (e) {
    $(".js-comment-modal").toggleClass("hidden")
  })


  $(".js-like-btn").on("click", function (e) {
    e.preventDefault();
    console.log("clicked")

    const action = $(this).attr("data-action");
    const url = $(this).data("url");
    const commentId = $(this).data("comment");
    console.log(commentId, action, url)

    $.ajax({
      type: 'POST',
      url: url,
      data: {
        action: action,
        comment_id: commentId,
      },

      success: (data) => {
        console.log("Success:", data);
        console.log("ID:", data.comment_id)

        const likeButton = $(`.js-like-btn[data-comment="${commentId}"]`);


        if (action == 'like') {
          likeButton.attr("data-action", "unlike");
          likeButton.addClass(data.class).removeClass("text-gray-200");
        } else {
          likeButton.attr("data-action", "like");
          likeButton.addClass(data.class).removeClass("text-red-500");
        }
      },
      error: (error) => {
        console.log('error')
      }
    });
  })




  $('.js-reply-button').click(function () {
    var CompositionId = $("section.composition-element").data('composition-id')
    var parentId = $(this).data('comment-id');
    $('#id_commenting_to').val(CompositionId);
    $('#id_parent').val(parentId);
  });
});
