from packets.factories import MessageFactory
from packets.Messages.Client.LoginMessage import LoginMessage
from packets.Messages.Client.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from packets.Messages.Client.VisitHomeMessage import VisitHomeMessage

message_factory = MessageFactory()
#command_factory = CommandFactory()

message_factory[18101] = LoginMessage
message_factory[10212] = ChangeAvatarNameMessage
message_factory[14600] = ChangeAvatarNameMessage
message_factory[14113] = VisitHomeMessage

#command_factory[14102] = None # EndClientTurnMessage

# message_factory[packet_id] = class_of_this_packet
