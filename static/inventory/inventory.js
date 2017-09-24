// Поиск по инвентори
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
       
       	//Добавление новой ноды
	$("#btn_new_node").click(function(event){
		var add_new_node = $("#new_node_form").serialize(); //Формируем массив
		console.log( add_new_node );
	 	$.ajax({
                 type:"GET",
                 url:"new_node/",
                 data: add_new_node ,
                 success: function(data){
                     $("#result_new_node").html(data) 
                    }
        });
	});
	
});
