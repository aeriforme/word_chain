$(document).ready(function(){
    $('#load_data').click(function(){
     $.ajax({
      url:"words.csv",
      dataType:"text",
      success:function(data)
      {
       var words_data = data.split(/\r?\n|\r/);
       var table_data = '<table class="table table-bordered table-striped">';
       
       var shuffled_words_data = shuffle(words_data);

       for(var count = 0; count<words_data.length; count++)
       {


        var cell_data = shuffled_words_data[count].split(",");
        table_data += '<tr>';
        for(var cell_count=0; cell_count<cell_data.length; cell_count++)
        {
         if(count === 0)
         {
          table_data += '<th>'+cell_data[cell_count]+'</th>';
         }
         else
         {
          table_data += '<td>'+cell_data[cell_count]+'</td>';
         }
        }
        table_data += '</tr>';
       }
       table_data += '</table>';
       $('#words_table').html(table_data);
      }
     });
    });
    
   });


   function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle...
    while (currentIndex != 0) {
  
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
  }
  