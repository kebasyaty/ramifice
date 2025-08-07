::: ramifice.models
    options:
      members: no

<hr>

#### Model Parameters

See the documentation [here](https://kebasyaty.github.io/ramifice/ "here").

###### ( only `service_name` is a required parameter )

<div>
   <table>
     <tr>
       <th align="left">Parameter</th>
       <th align="left">Default</th>
       <th align="left">Description</th>
     </tr>
     <tr>
       <td align="left">service_name</td>
       <td align="left">no</td>
       <td align="left"><b>Examples:</b> Accounts | Smartphones | Washing machines | etc ... </td>
     </tr>
     <tr>
       <td align="left">fixture_name</td>
       <td align="left">None</td>
       <td align="left">
         The name of the fixture in the <b>config/fixtures</b> directory (without extension).
         <br>
         <b>Examples:</b> SiteSettings | AppSettings | etc ...
       </td>
     </tr>
     <tr>
       <td align="left">db_query_docs_limit</td>
       <td align="left">1000</td>
       <td align="left">limiting query results.</td>
     </tr>
     <tr>
       <td align="left">is_create_doc</td>
       <td align="left">True</td>
       <td align="left">
         Can a Model create new documents in a collection?<br>
         Set to <b>False</b> if you only need one document in the collection and the Model is using a fixture.
       </td>
     </tr>
     <tr>
       <td align="left">is_update_doc</td>
       <td align="left">True</td>
       <td align="left">Can a Model update documents in a collection?</td>
     </tr>
     <tr>
       <td align="left">is_delete_doc</td>
       <td align="left">True</td>
       <td align="left">Can a Model remove documents from a collection?</td>
     </tr>
   </table>
</div>

<br>

**Example:**

```python
@model(
    service_name="ServiceName",
    fixture_name="FixtureName",
    db_query_docs_limit=1000,
    is_create_doc = True,
    is_update_doc = True,
    is_delete_doc = True,
)
class User:
    def fields(self):
        self.username = TextField(
            label=gettext("Username"),
            required=True,
            unique=True,
        )
```

<hr>
