import assistant
import view
import viewmodel

def start():
		while True:
				choice = view.main_menu() # Меню
				match choice:
						case 1: # Открыть
								viewmodel.open_pb()
								view.print_message(assistant.load_successful)
						case 2: # Записать
								viewmodel.save_pb()
								view.print_message(assistant.save_successful)
						case 3: # Показать контакт
								pb = viewmodel.get_pb()
								view.print_contacts(pb, assistant.load_error)
						case 4: # Добавить контакт 
								contact = view.input_contact(assistant.input_new_contact, assistant.cancel_input)
								name = viewmodel.add_contact(contact)
								view.print_message(assistant.new_contact_successful(name))
						case 5: # Найти контакт
								word = view.input_search(assistant.input_search)
								result = viewmodel.search_pb(word)
								view.print_contacts(result, assistant.empty_search(word))
						case 6: # Изменить контакт
								pb = viewmodel.get_pb()
								index = view.input_index(assistant.input_index, pb, assistant.load_error)
								contact = view.input_contact(assistant.input_new_contact, assistant.cancel_input)
								result = viewmodel.change_pb(contact, index)
								view.print_message(assistant.change_successful(contact))
						case 7: # Удалить контакт 
								pb = viewmodel.get_pb()
								index = view.input_index(assistant.index_del_contact, pb, assistant.load_error)
								name = viewmodel.del_contact(index)
								view.print_message(assistant.del_contact(name))
						case 8:
								break