$( document ).ready(function() {
	//Обработчик для клика по кнопке
	 $("#search_form").click(function(event){
       var form_data = $("#search_form").serialize(); //Формируем массив
		console.log( form_data );
            $.ajax({
                 type:"GET",
                 url:"search/",
                 data: form_data ,
                 success: function(data){
                     $('#result_search').html(data) 
                    }
            });
       });
      //Обработчик для клика по Enter
	 $("#search_form").submit(function(event){
       var form_data = $("#search_form").serialize(); //Формируем массив
		console.log( form_data );
            $.ajax({
                 type:"GET",
                 url:"search/",
                 data: form_data ,
                 success: function(data){
                     $('#result_search').html(data) 
                    }
            });
            return false; //Отключаем перезагрузку страницы при отправке формы
       });
     //Обработчик для отправки во время набора текста
	 $("#search_form").keypress(function(event){
       var form_data = $("#search_form").serialize(); //Формируем массив
		console.log( form_data );
            $.ajax({
                 type:"GET",
                 url:"search/",
                 data: form_data ,
                 success: function(data){
                     $('#result_search').html(data) 
                    }
            });
       });

	   var field = $('#list').find('option');
	$(".chosen-container ").css({width: "95%"});
});